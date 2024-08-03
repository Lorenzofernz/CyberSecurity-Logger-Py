import logging
logging.basicConfig(filename='cybersecurity.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def log_event(event_type, message):
    if event_type == 'info':
        logging.info(message)
    elif event_type == 'error':
        logging.error(message)
    elif event_type == 'warning':
        logging.warning(message)
    else:
        logging.info("Uknown event type: " + message)
        
def analyze_logs():
    with open('cybersecurity.log', 'r') as file:
        for line in file:
            if 'ERROR' in line:
                print(f'Security Alert: {line}')
                
if __name__ == "__main__":
    log_event('INFO', 'System boot')
    log_event('ERROR', 'Unauthorized access attempt detected')
    analyze_logs()