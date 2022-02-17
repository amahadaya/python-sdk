# MessageRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | Phone number to use as the sender. This must be an incoming phone number that you have purchased from FreeClimb. | 
**to** | **str** | Phone number to receive the message. Must be within FreeClimb&#39;s service area. | 
**text** | **str** | Text contained in the message (maximum 160 characters).   **Note:** For text, only ASCII characters are supported. | 
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**notification_url** | **str** | When the Message changes status, this URL is invoked using HTTP POST with the messageStatus parameters.  **Note:** This is a notification only; any PerCL returned is ignored. | [optional] 
**account_id** | **str** | String that uniquely identifies this account resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


