ECHO is on.
Webjson - This is an interpreter which can generate the python code for website automation testing.

Input
JSON format files for the following resources

- Locators
- Logical Structures
- Page Objects

Output
Auto Generated Python code to perform the required actions on the corresponding locators as specified in the page objects

Section 1
Locator Json File

Input - Locator Json File
Output - Generated Python Code containing all the corresponding locator classes

type - locator
page

- name - Name of the generated file
config (List of object class of locator classes)
- type - As of now, always it is a collection
- verbose_name - Name of the generated Class
- members - List of the locators as part of the class
	- id - Id of the locator, which will be used in the page object json
	- type - locator (for static) or dynamic (for dynamic locator)
	- verbose_name - It will be generated with this name. Usually, it is same as id but it can be different
	- locator - id or xpath of the corresponding locator
	- locator_type - It can be either id or xpath

Example Locator Config File
{
    "type": "locator",
    "page": {
        "name": "admin_client_add",
    },
    "config": [
        {
            "type": "collection",
            "verbose_name": "AdminClientAddLocator",
            "members": [
                {
                    "id": "client_active_table_id",
                    "type": "locator",
                    "verbose_name": "client_active_table_id",
                    "locator": "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/table",
                    "locator_type": "xpath"
                },
                {
                    "id": "client_add_btn",
                    "type": "locator",
                    "verbose_name": "client_add_btn",
                    "locator": "/html/body/div[1]/div/div/div/div/div[1]/div[1]/h6/button",
                    "locator_type": "xpath"
                },
                {
                    "id": "client_first_name",
                    "type": "locator",
                    "verbose_name": "first_name",
                    "locator": "/html/body/div[2]/div/div/div/div[2]/div[1]/input",
                    "locator_type": "xpath"
                }
            ]
        },
        {
            "type": "collection",
            "verbose_name": "ClientDashboardLink",
            "members": [
                {
                    "id": "client_fname_dynamic_locator",
                    "type": "dynamic",
                    "verbose_name": "client_fname_dynamic_locator",
                    "locator": "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/table/tbody/tr[{}]/td[2]/a",
                                /html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/a
                                /html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/table/tbody/tr[2]/td[2]/a
(Do not add the above 2 lines. This is for illustration purpose of how to fill in the "dynamic" locator)
                    "locator_type": "xpath",
                    "params": [
                        "row_num->int"
                    ]
                }
            ]
        }
    ]
}

Section 2
Logical Structure Json File

Input - Logical Structure Json File
Output - Generated Python Code containing all the logical data structure Json file

This is optional and needs to be done if and only if there is a need to group different values into a single structure

type - It must be specified as  "struct"
verbose_name - Name of the generated file
config (List of the logical structures which needs to be genearted as part of this file)
- verbose_name - Name of the generated class
- params - List of params containing the name of the fields along with the data types as part of this structure
	- The type of the param can be basic type (str, int, bool) or reference to other structure.
Caveats
- All dependent structures must be part of the same file (for instance client and its business)
- The parent structure must be defined before it is referenced in the child structure (for instance client must be defined before it is being referenced in the business)

config
{
    "type": "struct",
    "verbose_name": "ClientStruct",
    "config": [
        {
            "verbose_name": "Client",
            "params": ["first_name->str", "last_name->str", "email->str", "phone_num->str"]
        },
        {
            "verbose_name": "Business",
            "params": ["client_obj->Client"]
        }
    ]
}

Section 3
Page Object Json File

Input - Page Object Json File
Output - Generated Python Code containing all the page object/test case functions. This can be used to automate the test cases

type - page_objects
verbose_name - Name of the generated file
config (List of generated functions to be part of the page objects file)

- verbose_name - Name of the function
- params - parameters of this function (basic data type, logical data structure, support for list for both basic/logical data structure)
- return_type - return type of the function (can be basic data type or logical data structure)
- actions - List of actions, part of the function (supports - single action, repeat action, if/else action with multiple keywords associated to each action)
- keyword(s) - click, input_text, init_list, table_search, table_row_search, return
Caveats
- Nested repeats are not supported (repeat inside of repeat)
- Nested if are not supported
- if/else cannot contain the repeat (if/else cannot have a loop)
- Repeat can contain the if/else construct (if/else inside of for loop)

Keywords
- click - Used for clicking butons, checkbox et al
- input_text - Typically used for form fields (which are strings like first name et al)
- init_list - To make a list of a standard data-type (str, int, bool) or var (logical structure types).
- return - To return a specific value from a function
- table_search - Typically used for bulk validation
- table_row_search - Typlically used for dynamic locators

locator_id
- Locator Id on which the action needs to be performed
- Used by click, input_text, table_search, table_row_search

params
- Parameters of the corresponding keyword
- Used by input_text(1), init_list(1), return(1), table_search(3), table_row_search(3)

var_name
- Capture the return value of keyword in a variable

Constructs:
=====================================================================================================================================
=====================================================================================================================================
repeat - simulates a for loop. It needs the object and steps. Steps will contain list of any of the keywords described above.
{
	"repeat": {
		"object": "client_obj",
			"steps": [
			{
				"keyword": "click",
				"locator_id": "client_add_btn"
			},
			{
				"keyword": "input_text",
				"locator_id": "client_first_name",
				"params": [
					"client_obj.first_name::var"
				]
			},
			{
				"keyword": "input_text",
				"locator_id": "client_last_name",
				"params": [
					"client_obj.last_name::var"
				]
			},
			{
				"keyword": "input_text",
				"locator_id": "client_email",
				"params": [
					"client_obj.email::var"
				]
			},
			{
				"keyword": "input_text",
				"locator_id": "client_phone_number",
				"params": [
					"client_obj.phone_num::var"
				]
			},
			{
				"keyword": "click",
				"locator_id": "client_submit_btn"
			}
		]
	}
}
=====================================================================================================================================
=====================================================================================================================================
if/else - simulates the if/else. It needs condition and the steps to be inside of condition. Steps will contain list of any of the ketworks described above.
else is an optional structure.
{
	"if": {
		"condition": "random::var == True::bool",
			"steps": [
			{
				"keyword": "click",
				"locator_id": "client_option"
			}
			]
	},
	"else": {
			"steps": [
			{
				"keyword": "click",
				"locator_id": "client_option"
			}
			]
	}
}
=====================================================================================================================================
=====================================================================================================================================
keyword click example
{
	"keyword": "click",
	"locator_id": "client_add_btn"
}
=====================================================================================================================================
=====================================================================================================================================
keywork input_text example
{
	"keyword": "input_text",
	"locator_id": "client_first_name",
	"params": [
		"client_obj.first_name::var"
	]
}
=====================================================================================================================================
=====================================================================================================================================
keyword return example
{
	"keyword": "return",
	"params": [
		"return_val::var"
	]
}
=====================================================================================================================================
=====================================================================================================================================
keyword init_list example
{
	"keyword": "init_list",
	"params": [
		"Email::str"
	],
	"var_name": "l_col"
}
=====================================================================================================================================
=====================================================================================================================================
keyword table_search example
{
	"keyword": "table_search",
		"locator_id": "client_active_table_id",
		"params": [
			"l_col::var", "l_field::var", "client_objs::var"
		],
		"var_name": "return_val"
}
=====================================================================================================================================
=====================================================================================================================================
keyword table_row_search example
{
	"keyword": "table_row_search",
		"locator_id": "dynamic_locator",
		"locator_params": [
			"dummy::str", "234::int"
		],
		"params": [
			"l_col::var", "l_field::var", "client_obj::var"
		],
		"var_name": "row_num"
}
=====================================================================================================================================
=====================================================================================================================================
Overall Example
{
    "type": "page_object",
    "verbose_name": "AddClient",
    "config": [
        {
            "verbose_name": "add_client",
            "params": [
                "client_obj->Client::List"
            ],
            "return_type": "bool",
            "actions": [
                {
                    "keyword": "init_list",
                    "params": [
                        "Email::str"
                    ],
                    "var_name": "l_col"
                },
                {
                    "keyword": "init_list",
                    "params": [
                        "email::str"
                    ],
                    "var_name": "l_field"
                },
                {
                    "repeat": {
                        "object": "client_obj",
                        "steps": [
                            {
                                "keyword": "click",
                                "locator_id": "client_add_btn"
                            },
                            {
                                "keyword": "input_text",
                                "locator_id": "client_first_name",
                                "params": [
                                    "client_obj.first_name::var"
                                ]
                            },
                            {
                                "keyword": "input_text",
                                "locator_id": "client_last_name",
                                "params": [
                                    "client_obj.last_name::var"
                                ]
                            },
                            {
                                "keyword": "input_text",
                                "locator_id": "client_email",
                                "params": [
                                    "client_obj.email::var"
                                ]
                            },
                            {
                                "keyword": "input_text",
                                "locator_id": "client_phone_number",
                                "params": [
                                    "client_obj.phone_num::var"
                                ]
                            },
                            {
                                "keyword": "click",
                                "locator_id": "client_submit_btn"
                            }
                        ]
                    }
                },
                {
                    "keyword": "table_search",
                    "locator_id": "client_active_table_id",
                    "params": [
                        "l_col::var", "l_field::var", "client_objs::var"
                    ],
                    "var_name": "return_val"
                },
                {
                    "keyword": "return",
                    "params": [
                        "return_val::var"
                    ]
                }
            ]
        },
        {
            "verbose_name": "signin",
            "params": [
                "username->str",
                "password->str"
            ],
            "actions": [
                {
                    "keyword": "input_text",
                    "locator_id": "username",
                    "params": [
                        "username::var"
                    ]
                },
                {
                    "keyword": "input_text",
                    "locator_id": "password",
                    "params": [
                        "password::var"
                    ]
                },
                {
                    "keyword": "click",
                    "locator_id": "signin_btn"
                },
                {
                    "keyword": "init_list",
                    "params": [
                        "False::bool",
                        "False::bool"
                    ],
                    "var_name": "l_bool"
                }
            ]
        },
        {
            "verbose_name": "navigate_client",
            "params": [],
            "actions": [
                {
                    "keyword": "click",
                    "locator_id": "client_option"
                }
            ]
        }
    ]
}