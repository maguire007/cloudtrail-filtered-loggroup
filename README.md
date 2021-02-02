# cloudtrail-filtered-loggroup


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
