# MessageResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str** | String that uniquely identifies this account resource. | [optional] 
**message_id** | **str** | String that uniquely identifies this message resource | [optional] 
**status** | **str** | Indicates the state of the message through the message lifecycle including: new, queued, rejected, sending, sent, failed, received | [optional] 
**_from** | **str** | Phone number in E.164 format that sent the message. | [optional] 
**to** | **str** | Phone number in E.164 format that received the message. | [optional] 
**text** | **str** | Message contents | [optional] 
**direction** | **str** | Noting whether the message was inbound or outbound | [optional] 
**notification_url** | **str** | URL invoked when message sent | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


