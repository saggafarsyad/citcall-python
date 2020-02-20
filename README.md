# citcall-python

Citcall REST API for Python. API support for Synchchronous Miscall, Asynchronous miscall, and SMS.

This is the Python3 client library for use Citcall's API. To use this, you'll need a Citcall account and Your IP has been filtered in citcall system. See [citcall documentation](https://docs.citcall.com/) for more information. This is currently a beta release.


## Instalation

### Install Using PIP
```bash
pip install citcall-devel
```
### Install Source from GitHub

```bash
$ git clone git://github.com/citcall/citcall-python.git
``` 
Remember to note that the citcall folder is a package.


## Usage

```python
from citcall import Citcall
```
Create Object
```python
citcall = Citcall("userid","APIKEY")
```
***OR***

```python
import citcall
```
Create Object
```python
citcall = citcall.Citcall("userid","APIKEY")
```


## Example

### Miscall OTP

To use [Citcall's Miscall Async API](https://docs.citcall.com/async/) to Asynchronous miscall, call the `citcall.async_miscall()` method.

The API can be called directly, using a simple array of parameters, the keys match the [parameters of the API](https://docs.citcall.com/async/).

```python
motp = citcall.async_miscall({"msisdn":MSISDN,"gateway":gateway})
```
If you want to able to do verify later use this example.
```python
motp = citcall.async_miscall({"msisdn":MSISDN,"gateway":gateway,"valid_time":valid_time,"limit_try":limit_try})

```
Sync
```python
motp = citcall.sync_miscall({"msisdn":MSISDN,"gateway":gateway})
```
```python
motp = citcall.sync_miscall({"msisdn":MSISDN,"gateway":gateway,"valid_time":valid_time,"limit_try":limit_try})
```
The API response data can be accessed as dictonary
```python
print(motp)
```
### SMS
To use [Citcall's SMS API](https://docs.citcall.com/#sms) to send an SMS message, call the `citcall.sms()` method.

The API can be called directly, using a simple array of parameters, the keys match the [parameters of the API](https://docs.citcall.com/#sms).

```python
sms = citcall.sms({"senderid":"citcall","msisdn":MSISDN,"text":"Test message from the Citcall Python :p"})
```
The API response data can be accessed as dictonary

```python
print(sms)
```
## Contribute

1.  Check for open issues or open a new issue for a feature request or a bug
2.  Fork [the repository](https://github.com/citcall/citcall-python) on Github to start making your changes to the `master` branch (or branch off of it)
3.  Write a test which shows that the bug was fixed or that the feature works as expected
4.  Send a pull request and bug us until We merge it

