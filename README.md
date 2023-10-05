# sample-django-structure
Structure sample django for microservice

This sample include middleware to overwrite format response for service.
API return format:

{
    transaction_id: uuid // transaction of request,
    status_code: 200 // for success,
    message: "SUCCESS",
    data: object // data response
}

when API error. The exception will alias to ErrorMassage before response

{
    error_message: "SAMPLE-00000500" // look at ErrorMassage.py. Prefix SAMPLE is name service
    statusCode: 500 // look at ErrorMassage.py
    error_code: "SOMETHING_ERROR" // the code which you handle in your code
    message: "Detail error"
}

If you want to use right to allow access to API. Use @Authority.requires_rights() 

Infrastrure folder:
```
├── manage.py 				    run project
├── server 					    folder server app
│   ├── setting.py 				config env
│   ├── constants 			    store constant variable
│   │   ├── ErrorMessage.py 	store error code to handle error
│   ├── middlewares 		    store middleware layer
│   │   ├── Authority.py 	    store functions to check authen
│   │   ├── HandleError.py 		store functions to handle format output error api
│   │   ├── HandleSuccess.py 	store functions to handle format output success api
│   ├── custom_midleware.py     package install middleware folder
│   ├── urls.py                 register router blueprint
├── users                       package module. Ex: users module
```

