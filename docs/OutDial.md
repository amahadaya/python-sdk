# OutDial

The OutDial command is used to call a phone number
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** | URL to which FreeClimb sends an HTTP POST request.  | 
**call_connect_url** | **str** | URL to which FreeClimb makes an HTTP POST request informing the result of the OutDial. | 
**calling_number** | **float** | he caller ID to show to the called party when FreeClimb calls. This can be one of the following: The To or From number provided in the first Webhook to your webserver. Any phone number you have purchased from FreeClimb. | 
**destination** | **float** | E.164 representation of the phone number to Call.  | 
**if_machine** | [**IfMachine**](IfMachine.md) |  | [optional] 
**if_machine_url** | **str** | When the &#x60;ifMachine&#x60; flag is set to &#x60;redirect&#x60;, this attribute specifies a URL to which FreeClimb makes a POST request when an answering machine or a fax machine is detected. This URL is required if the &#x60;ifMachine&#x60; flag is set to &#x60;redirect&#x60;. Otherwise, it should not be included. | [optional] 
**send_digits** | **str** | DTMF tones to play to the outdialed Call. This is typically used to dial a number and then dial an extension. | [optional] 
**status_callback_url** | **str** | When the outdialed Call leg terminates, FreeClimb sends a &#x60;callStatus&#x60; Webhook to the &#x60;statusCallbackUrl&#x60;. This is a notification only; any PerCL command returned is ignored. | [optional] 
**timeout** | **int** | Maximum time in seconds the &#x60;OutDial&#x60; command waits for the called party to answer the Call. When a timeout occurs, FreeClimb invokes the &#x60;callConnectUrl&#x60; Webhook to report that the out-dialed Call has ended with a status of &#x60;noAnswer&#x60;. | [optional] 
**privacy_mode** | **bool** | Parameter &#x60;privacyMode&#x60; will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 
**command** | **str** | Name of PerCL Command (this is automatically derived from mapping configuration and should not be manually supplied in any arguments) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


