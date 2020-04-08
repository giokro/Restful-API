# Data Registry Service

## Usage

### List all product categories

**Definition**

`GET /categories`

**Response**

- `200 OK` on success

```json
{
    "categories": [
        "Lamps",
        "Jars",
        "Cups"
    ]
}
```


### List of products in a category

**Definition**

`GET /categories/<category>`

**Response**
- `404 Not Found` if category doesn't exist
- `200 OK` on success

```json
{
    "IT College": [
        "Advanced Networking",
        "IT Infrastructure Management",
        "Machine Learning",
        "Linux Administration"
    ]
}
```

#######################################

### Create a category

**Definition**

`POST /categories`

**Arguments**

- "identifier": "string" 


**Response**

- `201 Created` on success
- `409 Conflict` if already exists
- `400 Bad Request` if argument error

```json
{
    "Inserted": "SOC"
}
```



### Update a category

**Definition**

`PUT /categories/<identifier>`

**Arguments**

- "identifier": "string"
- "replacement": "string"

**Response**

- `404 Not Found` if doesn't exist
- `400 Bad Request` if argument error
- `201 Created` on success

```json
{
    "Updated": "Nodari",
    "Replacement": "Nugo"
}
```



### Delete a category

**Definition**

`DELETE /categories/<identifier>`

**Response**

- `400 Bad Request` if argument error
- `204 No Content` on success

```json
{
    "Deleted": "Nodari"
}
```


#######################################

### Create a product

**Definition**

`POST /categories/<identifier>`

**Arguments**

- "identifier": "string" 

**Response**

- `201 Created` on success
- `409 Conflict` if already exists
- `400 Bad Request` if argument error

```json
{
    "Inserted": "SOC"
}
```



### Update a product

**Definition**

`PUT /categories/<identifier>`

**Arguments**

- "identifier": "string"
- "replacement": "string"

**Response**

- `404 Not Found` if doesn't exist
- `400 Bad Request` if argument error
- `201 Created` on success

```json
{
    "Updated": "Nodari",
    "Replacement": "Nugo"
}
```



### Delete a category

**Definition**

`DELETE /categories/<identifier>`

**Response**

- `404 Not Found` if doesn't exist
- `400 Bad Request` if argument error
- `204 No Content` on success

```json
{
    "Deleted": "Nodari"
}
```

