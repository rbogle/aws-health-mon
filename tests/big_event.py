
test_event ={
    "message": {
        "successfulSet": [
            {
                "event": {
                    "arn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_WCDUM_1640176551",
                    "service": "EC2",
                    "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
                    "eventTypeCategory": "issue",
                    "region": "us-east-1",
                    "startTime": "2021-12-22 12:35:51.788000+00:00",
                    "endTime": "2021-12-23 00:22:31+00:00",
                    "lastUpdatedTime": "2021-12-23 00:54:12.226000+00:00",
                    "statusCode": "closed",
                    "eventScopeCode": "PUBLIC"
                },
                "eventDescription": {
                    "latestDescription": "[RESOLVED] API Error Rates\n\n[04:35 AM PST] We are investigating increased EC2 launch failures and networking connectivity issues for some instances in a single Availability Zone (USE1-AZ4) in the US-EAST-1 Region. Other Availability Zones within the US-EAST-1 Region are not affected by this issue.\n\n[05:01 AM PST] We can confirm a loss of power within a single data center within a single Availability Zone (USE1-AZ4) in the US-EAST-1 Region. This is affecting availability and connectivity to EC2 instances that are part of the affected data center within the affected Availability Zone. We are also experiencing elevated RunInstance API error rates for launches within the affected Availability Zone. Connectivity and power to other data centers within the affected Availability Zone, or other Availability Zones within the US-EAST-1 Region are not affected by this issue, but we would recommend failing away from the affected Availability Zone (USE1-AZ4) if you are able to do so. We continue to work to address the issue and restore power within the affected data center.\n\n[05:18 AM PST] We continue to make progress in restoring power to the affected data center within the affected Availability Zone (USE1-AZ4) in the US-EAST-1 Region. We have now restored power to the majority of instances and networking devices within the affected data center and are starting to see some early signs of recovery. Customers experiencing connectivity or instance availability issues within the affected Availability Zone, should start to see some recovery as power is restored to the affected data center. RunInstances API error rates are returning to normal levels and we are working to recover affected EC2 instances and EBS volumes. While we would expect continued improvement over the coming hour, we would still recommend failing away from the Availability Zone if you are able to do so to mitigate this issue.\n\n[05:39 AM PST] We have now restored power to all instances and network devices within the affected data center and are seeing recovery for the majority of EC2 instances and EBS volumes within the affected Availability Zone. Network connectivity within the affected Availability Zone has also returned to normal levels. While all services are starting to see meaningful recovery, services which were hosting endpoints within the affected data center - such as single-AZ RDS databases, ElastiCache, etc. - would have seen impact during the event, but are starting to see recovery now. Given the level of recovery, if you have not yet failed away from the affected Availability Zone, you should be starting to see recovery at this stage. \n\n[06:13 AM PST] We have now restored power to all instances and network devices within the affected data center and are seeing recovery for the majority of EC2 instances and EBS volumes within the affected Availability Zone. We continue to make progress in recovering the remaining EC2 instances and EBS volumes within the affected Availability Zone. If you are able to relaunch affected EC2 instances within the affected Availability Zone, that may help to speed up recovery. We have a small number of affected EBS volumes that are still experiencing degraded IO performance that we are working to recover. The majority of AWS services have also recovered, but services which host endpoints within the customer’s VPCs - such as single-AZ RDS databases, ElasticCache, Redshift, etc. - continue to see some impact as we work towards full recovery. \n\n[06:51 AM PST] We have now restored power to all instances and network devices within the affected data center and are seeing recovery for the majority of EC2 instances and EBS volumes within the affected Availability Zone. For the remaining EC2 instances, we are experiencing some network connectivity issues, which is slowing down full recovery. We believe we understand why this is the case and are working on a resolution. Once resolved, we expect to see faster recovery for the remaining EC2 instances and EBS volumes. If you are able to relaunch affected EC2 instances within the affected Availability Zone, that may help to speed up recovery. Note that restarting an instance at this stage will not help as a restart does not change the underlying hardware. We have a small number of affected EBS volumes that are still experiencing degraded IO performance that we are working to recover. The majority of AWS services have also recovered, but services which host endpoints within the customer’s VPCs - such as single-AZ RDS databases, ElasticCache, Redshift, etc. - continue to see some impact as we work towards full recovery. \n\n[08:02 AM PST] Power continues to be stable within the affected data center within the affected Availability Zone (USE1-AZ4) in the US-EAST-1 Region. We have been working to resolve the connectivity issues that the remaining EC2 instances and EBS volumes are experiencing in the affected data center, which is part of a single Availability Zone (USE1-AZ4) in the US-EAST-1 Region. We have addressed the connectivity issue for the affected EBS volumes, which are now starting to see further recovery. We continue to work on mitigating the networking impact for EC2 instances within the affected data center, and expect to see further recovery there starting in the next 30 minutes. Since the EC2 APIs have been healthy for some time within the affected Availability Zone, the fastest path to recovery now would be to relaunch affected EC2 instances within the affected Availability Zone or other Availability Zones within the region.\n\n[09:28 AM PST] We continue to make progress in restoring connectivity to the remaining EC2 instances and EBS volumes. In the last hour, we have restored underlying connectivity to the majority of the remaining EC2 instance and EBS volumes, but are now working through full recovery at the host level. The majority of affected AWS services remain in recovery and we have seen recovery for the majority of single-AZ RDS databases that were affected by the event. If you are able to relaunch affected EC2 instances within the affected Availability Zone, that may help to speed up recovery. Note that restarting an instance at this stage will not help as a restart does not change the underlying hardware. We continue to work towards full recovery.\n\n[11:08 AM PST] We continue to make progress in restoring power and connectivity to the remaining EC2 instances and EBS volumes, although recovery of the remaining instances and volumes is taking longer than expected. We believe this is related to the way in which the data center lost power, which has led to failures in the underlying hardware that we are working to recover. While EC2 instances and EBS volumes that have recovered continue to operate normally within the affected data center, we are working to replace hardware components for the recovery of the remaining EC2 instances and EBS volumes. We have multiple engineers working on the underlying hardware failures and expect to see recovery over the next few hours. As is often the case with a loss of power, there may be some hardware that is not recoverable, and so we continue to recommend that you relaunch your EC2 instance, or recreate you EBS volume from a snapshot, if you are able to do so.\n\n[12:03 PM PST] Over the last hour, after addressing many of the underlying hardware failures, we have seen an accelerated rate of recovery for the affected EC2 instances and EBS volumes. We continue to work on addressing the underlying hardware failures that are preventing the remaining EC2 instances and EBS volumes. For customers that continue to have EC2 instance or EBS volume impairments, relaunching affected EC2 instances or recreating affecting EBS volumes within the affected Availability Zone, continues to be a faster path to full recovery. \n\n[01:39 PM PST] We continue to make progress in addressing the hardware failures that are delaying recovery of the remaining EC2 instances and EBS volumes. At this stage, if you are still waiting for an EC2 instance or EBS volume to fully recover, we would strongly recommend that you consider relaunching the EC2 instance or recreating the EBS volume from a snapshot. As is often the case with a loss of power, there may be some hardware that is not recoverable, which will prevent us from fully recovering the affected EC2 instances and EBS volumes. We are not quite at that point yet in terms of recovery, but it is unlikely that we will recover all of the small number of remaining EC2 instances and EBS volumes. If you need help in launching new EC2 instances or recreating EBS volumes, please reach out to AWS Support.\n\n[03:13 PM PST] Since the last update, we have more than halved the number of affected EC2 instances and EBS volumes and continue to work on the remaining EC2 instances and EBS volumes. The remaining EC2 instances and EBS volumes have all experienced underlying hardware failures due to the nature of the initial power event, which we are working to resolve. We expect to make further progress on this list within the next hour, but some of the remaining EC2 instances and EBS volumes may not be recoverable due to hardware failures. If you have the ability to relaunch an affected EC2 instance or recreate an affected EBS volume from snapshot, we continue to strongly recommend that you take that path.\n\n[04:22 PM PST] Starting at 4:11 AM PST some EC2 instances and EBS volumes experienced a loss of power in a single data center within a single Availability Zone (USE1-AZ4) in the US-EAST-1 Region. Instances in other data centers within the affected Availability Zone, and other Availability Zones within the US-EAST-1 Region were not affected by this event. At 4:55 AM PST, power was restored to EC2 instances and EBS volumes in the affected data center, which allowed the majority of EC2 instances and EBS volumes to recover. However, due to the nature of the power event, some of the underlying hardware experienced failures, which needed to be resolved by engineers within the facility. Engineers worked to recover the remaining EC2 instances and EBS volumes affected by the issue. By 2:30 PM PST, we recovered the vast majority of EC2 instances and EBS volumes. However, some of the affected EC2 instances and EBS volumes were running on hardware that has been affected by the loss of power and is not recoverable. For customers still waiting for recovery of a specific EC2 instance or EBS volume, we recommend that you relaunch the instance or recreate the volume from a snapshot for full recovery. If you need further assistance, please contact AWS Support."
                }
            }
        ],
        "failedSet": [],
        "ResponseMetadata": {
            "RequestId": "339bb5d7-332d-44ff-84d3-6340868124c8",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid": "339bb5d7-332d-44ff-84d3-6340868124c8",
                "content-type": "application/x-amz-json-1.1",
                "content-length": "11124",
                "date": "Thu, 23 Dec 2021 01:25:51 GMT"
            },
            "RetryAttempts": 0
        }
    }
}