# QueueResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | ID of the account that created this Queue. | [optional] 
**queue_id** | **str, none_type** | A string that uniquely identifies this Queue resource. | [optional] 
**alias** | **str, none_type** | A description for this Queue. | [optional] 
**max_size** | **int, none_type** | The maximum number of Calls permitted in the Queue. Default is 100. Maximum is 1000. | [optional] 
**current_size** | **int, none_type** | Count of Calls currently in the Queue. | [optional] 
**average_queue_removal_time** | **int, none_type** | The average amount of time (in seconds) for a call to be removed from the queue. | [optional] 
**subresource_uris** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | List of subresources for this Queue (which includes Queue members). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


