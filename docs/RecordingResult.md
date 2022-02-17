# RecordingResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**recording_id** | **str, none_type** | String that uniquely identifies this recording resource. | [optional] 
**account_id** | **str, none_type** | ID of the account that created this recording. | [optional] 
**call_id** | **str, none_type** | ID of the Call that was recorded. If a Conference was recorded, this value is empty and the conferenceId property is populated. | [optional] 
**duration_sec** | **int, none_type** | Length of the recording in seconds. | [optional] 
**conference_id** | **str, none_type** | ID of the Conference that was recorded. If a Call was recorded, this value is empty and the callId property is populated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


