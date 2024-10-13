def file_exist(file_name):
    try:
        file = open(file_name, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def open_file_reading(file_name):
    try:
        file = open(file_name, 'r')
    except:
        print('Error! Could not open the file.')
    else:
        print(f'File {file_name} open to reading.')
        return file

def create_file(file_name):
    try:
        file = open(file_name, 'wt+')
        file.close()
    except:
        print("Error! The file wasn't created.")
    else:
        print(f'File {file_name} created successfully.')

def list_file(file_name):
    try:
        file = open(file_name, 'rt')
    except:
        print('Error reading the file.')
    else:
        data = file.readlines()
    finally:
        file.close()
        return data

def insert_score(file_name, player_name, score):
    try:
        file = open(file_name, 'at')
    except:
        print('Error opening the file.')
    else:
        file.write(f'{player_name}; {score}\n')
    finally:
        file.close()