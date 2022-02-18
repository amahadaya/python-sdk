# RecordingResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_id** | **str, none_type** | String that uniquely identifies this recording resource. | [optional] 
**account_id** | **str, none_type** | ID of the account that created this recording. | [optional] 
**call_id** | **str, none_type** | ID of the Call that was recorded. If a Conference was recorded, this value is empty and the conferenceId property is populated. | [optional] 
**duration_sec** | **int, none_type** | Length of the recording in seconds. | [optional] 
**conference_id** | **str, none_type** | ID of the Conference that was recorded. If a Call was recorded, this value is empty and the callId property is populated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


