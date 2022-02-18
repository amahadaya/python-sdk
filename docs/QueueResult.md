# QueueResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str, none_type** | ID of the account that created this Queue. | [optional] 
**queue_id** | **str, none_type** | A string that uniquely identifies this Queue resource. | [optional] 
**alias** | **str, none_type** | A description for this Queue. | [optional] 
**max_size** | **int, none_type** | The maximum number of Calls permitted in the Queue. Default is 100. Maximum is 1000. | [optional] 
**current_size** | **str, none_type** | Count of Calls currently in the Queue. | [optional] 
**average_wait_time** | **str, none_type** | Average wait time (in seconds) of all Calls in the Queue. | [optional] 
**subresource_uris** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | List of subresources for this Queue (which includes Queue members). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


