import argparse
from os.path import abspath


def get_args():
    '''Gets from console the path to the configuration file and the text file to be replaced.'''
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="Path to configuration file")
    parser.add_argument("text_file", type=str, help="The path to the file where you want to replace characters")
    return parser.parse_args()

def get_configuration(config_path : str):
    '''Parses a configuration file and makes a dictionary of the form: {'replaced' : 'replacing'} '''
    try:
        with open(abspath(config_path)) as f:
            config_lines=f.readlines()
    except FileNotFoundError:
        print('File of configuration not found. Please, check path or name file.')
        exit()
    except UnicodeDecodeError:
        print('Please check extension of the configuration file. Only .txt files can be specified')
        exit()
    list_of_replaced = []
    list_of_replacing = []
    for i in config_lines:
        list_of_replaced.append(i[0])
        try:
            list_of_replacing.append(i[2])
        except IndexError:
            print('Please check the contents of the configuration file. The lines in the file should have the form a = b.')
            exit()
    return dict(zip(list_of_replaced, list_of_replacing))

def get_text(text_file_path : str):
    '''Gets the text to be processed.'''
    try:
        with open(abspath(text_file_path)) as f:
            text_lines = f.readlines()
    except FileNotFoundError as e:
        print('File with text for processed not found. Please, check path or name file.')
        exit()
    except UnicodeDecodeError:
        print('Please check extension of the file with text for processed. Only .txt files can be specified.')
        exit()
    return text_lines

def processes_text(text_lines : list, list_of_replaced : list, list_of_replacing : list):
    '''Replaces characters in the text according to the config.'''
    processed_text = []
    for i in text_lines:
        for id, item in enumerate(list_of_replaced):
            i = i.replace(list_of_replaced[id], list_of_replacing[id])
        processed_text.append(i)
    return processed_text

def write_file(text_file_path : str, processed_text : list):
    '''Writes processed text to a file.'''
    with open(abspath(text_file_path), 'w') as f:
        for i in processed_text:
            f.write(i + '\n')

def delete_line_break(text : str):
    '''Removes line breaks.'''
    return ''.join(list(filter(lambda c: c!='\n', text)))

def invert_of_text(text : list):
    '''Overwrites text in reverse order.'''
    for id, item in enumerate(text):
        text[id] = item[::-1]
    return text[::-1]