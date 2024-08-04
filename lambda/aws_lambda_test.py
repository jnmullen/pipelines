import aws_lambda 


def test_capital_case():
    assert aws_lambda.lambda_capital_case('semaphore') == 'Semaphore'
