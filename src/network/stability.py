import subprocess
import time
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv()

# Getting the current date and time
current_datetime = datetime.now()
current_date_time = current_datetime.strftime("%H:%M:%S (%Y. %m. %d)")
logfile_date = current_datetime.strftime("%Y%m%d-%H%M%S")
logfile_name = logfile_date + "-network.log"


logging.basicConfig(filename=logfile_name, level=logging.DEBUG)


def ping_server(host, interval, count, threshold):
    # Infinity running
    infinity = False

    # If infinity running
    if count == 0:
        infinity = True
        count = 1

    # Set threshold count
    threshold_count = 0

    # Getting the current date and time
    current_datetime = datetime.now()
    current_date_time = current_datetime.strftime("%H:%M:%S (%Y. %m. %d)")

    # Show configuration
    print("##############################################")
    print(f"# Start time: {current_date_time}")
    print(f"# Destination server: {host}")
    print(f"# Threshold (lost ping): {threshold}")
    print(f"# Infinity running: {infinity}")
    print(f"# Ping count: {count}") if infinity == False else print(
        f"# Ping count: N/A"
    )
    print(f"# Ping interval: {interval}")
    print("##############################################")

    logging.info("##############################################")
    logging.info("# Start time: " + current_date_time)
    logging.info("# Destination server: " + host)
    logging.info("# Threshold (lost ping): " + str(threshold))
    logging.info("# Infinity running: " + str(infinity))
    logging.info("# Ping count: " + str(count)) if infinity == False else logging.info(
        "# Ping count: N/A"
    )
    logging.info("# Ping interval: " + str(interval))
    logging.info("##############################################")
    try:
        # Start measuring
        while count > 0:
            # Getting the current date and time
            current_datetime = datetime.now()
            current_date_time = current_datetime.strftime("%H:%M:%S (%Y. %m. %d)")

            try:
                result = subprocess.run(
                    ["ping", "-c", "1", host],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=10,
                )
                if result.returncode == 0:
                    logging.info(
                        str(current_date_time)
                        + "- Stability: Internet connection is stable to "
                        + host
                    )
                else:
                    logging.warning(
                        str(current_date_time)
                        + "- Stability: Internet connection is unstable to "
                        + host
                    )
                    threshold_count += 1
            except subprocess.TimeoutExpired:
                logging.error(
                    str(current_date_time)
                    + "- Stability: Timeout occurred while pinging "
                    + host
                )
                threshold_count += 1
            except Exception as e:
                logging.error(
                    str(current_date_time)
                    + "- Stability: Error occurred while pinging "
                    + host
                )
                threshold_count += 1

            # Check threshold
            if threshold_count >= int(threshold):
                # Turn off router
                logging.warning(
                    str(current_date_time)
                    + "- Threshold ("
                    + str(threshold)
                    + ") has been reached ("
                    + str(threshold_count)
                    + "). Start to fix internet connection"
                )
                
                # Get Pin count
                RELAY_CHANNEL_COUNT=os.getenv('RELAY_CHANNEL_COUNT')
                # Get Pin for relay 1
                PIN1 = os.getenv('RELAY_PIN_1')
                # Get Pin for relay 2
                PIN2 = os.getenv('RELAY_PIN_2')
                from ..digitalio import fixnetwork
                fixnetwork.switch_relay("OFF",int(PIN1),int(PIN2),int(RELAY_CHANNEL_COUNT))
                break

            time.sleep(interval)

            # Check infinity
            if infinity == False:
                count -= 1
    except KeyboardInterrupt:
        logging.info("##############################################")
        logging.warning(
            str(current_date_time) + "- **** User has terminated the process ****"
        )
        logging.info("##############################################")


if __name__ == "__main__":
    host_to_ping = os.getenv("NETWORK_STABILITY_HOST")  # Destination server to ping
    interval_seconds = int(
        os.getenv("NETWORK_STABILITY_PING_INTERVAL")
    )  # Time between ping
    ping_count = int(
        os.getenv("NETWORK_STABILITY_PING_COUNT")
    )  # Ping count (0: infinity)
    threshold_ping = int(
        os.getenv("NETWORK_STABILITY_THRESHOLD")
    )  # Threshold for lost ping before start to fox internet
    ping_server(host_to_ping, interval_seconds, ping_count, threshold_ping)
