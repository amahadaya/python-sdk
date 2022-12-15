# UpdateCallRequestStatus

Either `canceled` or `completed`.  Specifying `canceled` attempts to hang up calls that are queued without affecting calls already in progress. Specifying `completed` attempts to hang up a call already in progress.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Either &#x60;canceled&#x60; or &#x60;completed&#x60;.  Specifying &#x60;canceled&#x60; attempts to hang up calls that are queued without affecting calls already in progress. Specifying &#x60;completed&#x60; attempts to hang up a call already in progress. |  must be one of ["canceled", "completed", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


