# SetListen

The `SetListen` command enables or disables the listen privilege for a Conference Participant provided both calls are in the same conference. The Participant can hear what the other participants are saying only if this privilege is enabled.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | ID of the call leg that is to be assigned the listen privilege. The Call must be in a Conference or an error will be triggered. | 
**listen** | **bool** | Specifying &#x60;false&#x60; will silence the Conference for this Participant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


