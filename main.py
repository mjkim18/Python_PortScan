import os
import socket

# TODO add more imports here..

def main():
    print('Hello World!')

def successful_response_test(code):
    success_codes = [200, 201, 202, 203, 204, 205, 207, 208, 226]
    if code in success_codes:
        return True
    return False


if __name__ == '__main__':
    main()
