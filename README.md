# cloudtrail filtered logs to log group

Eventbridge rule and lambda trigger to filter cloudtrail logs and making them searchable with cloudwatch insights.

###
Supports filtering out the sourceip, and specific apis from the logs.


# Cloudwatch insights query



Event bridge rule pattern example


```
{
  "source": [
    "aws.cloudtrail",
    "aws.ec2",
    "aws.lambda",
    "aws.ecs",
    "aws.cloudformation"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "dynamodb.amazonaws.com",
      "ec2.amazonaws.com",
      "cloudtrail.amazonaws.com",
      "cloudformation.amazonaws.com"
    ]
  }
}

```

## CloudwatchInsights query


```
fields @timestamp,detail.eventName,source,detail.eventType,detail.userIdentity.principalId, detail.sourceIPAddress
|filter @message like /version/
| sort @timestamp desc
| limit 20


```
