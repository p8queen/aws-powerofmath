#aws lambda function,Math base to power
import math
import json

def lambda_handler(event, context):
    base = int(event['base'])
    exponent = int(event['exponent'])
    result = math.pow(base, exponent)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is: ' + str(result))
    }

#main
if __name__ == '__main__':
    print(lambda_handler({'base': 2, 'exponent': 3}, None))

