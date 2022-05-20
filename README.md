# Kanvas

It's a project where you can administrate your courses, adding students and instructors and add the address of them.

# Users

## POST /api/accounts/

This endpoint is to registrate the users.

Input:

```json
{
  "first_name": "eric",
  "last_name": "martins",
  "email": "eric@bol.com.br",
  "password": "1234",
  "is_admin": true
}
```

If the request is sucessfully(201 Created).

Output:

```json
{
  "first_name": "eric",
  "last_name": "martins",
  "email": "eric@bol.com.br",
  "is_admin": true
}
```

## POST /api/login/

This endpoint is to login whith user.

Input:

```json
{
  "email": "eric@bol.com.br",
  "password": "1234"
}
```

If the request is sucessfully(200 OK).

Output:

```json
{
  "token": "919e1c3a055ee5d0a2ccec2b93d62a3d90b0bbb1"
}
```

## GET /api/accounts/

This endpoint is to get all user, it's required to be a admin and the bearer autentication token.

Input:
Don't need Input.

If the request is sucessfully(200 OK).

Output:

```json
[
  {
    "uuid": "5d880acd-cad7-424d-9b23-dffa6aa10372",
    "first_name": "eric",
    "last_name": "martins",
    "email": "eric@bol.com.br",
    "is_admin": true
  }
]
```

# Address

## PUT /api/address/

This endpoint is to add a address to a user, it's not required to be a admin but the bearer autentication token is required.

Input:

```json
{
  "zip_code": "123456789",
  "street": "Rua das Flores",
  "house_number": "123",
  "city": "Curitiba",
  "state": "Paraná",
  "country": "Brasil"
}
```

If the request is sucessfully(200 OK).

Output:

```json
{
  "uuid": "38670659-ca2e-4906-a5e9-3fb93c18cccb",
  "street": "Rua das Flores",
  "house_number": 123.0,
  "city": "Curitiba",
  "state": "Paraná",
  "zip_code": "123456789",
  "country": "Brasil",
  "users": [
    {
      "uuid": "cd38010a-4b8d-4257-b160-761ed34bf183",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john_doe@bol.com.br",
      "is_admin": false
    }
  ]
}
```

# Courses

## POST /api/courses/

This endpoint is to create a course, it's required to be a admin and the bearer autentication token.

Input:

```json
{
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "https://gitlab.com/turma_django/"
}
```

If the request is sucessfully(201 Created).

Output:

```json
{
  "uuid": "db4ff40f-549d-4717-a205-5ef81dde6e5c",
  "name": "Django",
  "link_repo": "https://gitlab.com/turma_django/",
  "demo_time": "09:00:00",
  "created_at": "2022-05-17",
  "instructor": null,
  "students": []
}
```

## GET /api/courses/

This endpoint is to get all thr courses, it's not required to be a admin but the bearer autentication token is required.

Input:
Don't need input.

If the request is sucessfully(200 OK).

Output:

```json
[
  {
    "uuid": "dba4ab8b-77a3-4b6e-bc98-05d6e9f6c7dd",
    "name": "Django",
    "link_repo": "https://gitlab.com/turma_node/",
    "demo_time": "08:00:00",
    "created_at": "2022-05-17",
    "instructor": null,
    "students": []
  },
  {
    "uuid": "db4ff40f-549d-4717-a205-5ef81dde6e5c",
    "name": "Django",
    "link_repo": "https://gitlab.com/turma_django/",
    "demo_time": "09:00:00",
    "created_at": "2022-05-17",
    "instructor": null,
    "students": []
  }
]
```

## GET /api/courses/<course_id>/

This endpoint is to get a specific course, it's not required to be a admin but the bearer autentication token is required and the id must be pass in the url.

Input:
Don't need input

If the request is sucessfully(200 OK).

Output:

```json
{
  "uuid": "dba4ab8b-77a3-4b6e-bc98-05d6e9f6c7dd",
  "name": "Django",
  "link_repo": "https://gitlab.com/turma_node/",
  "demo_time": "08:00:00",
  "created_at": "2022-05-17",
  "instructor": null,
  "students": []
}
```

## PATCH /api/courses/<course_id>/

This endpoint is to update a specific course, it's required to be a admin, the bearer autentication token and the id must be pass in the url.

Input:

```json
{
  "name": "Django",
  "demo_time": "8:00",
  "link_repo": "https://gitlab.com/turma_node/"
}
```

If the request is sucessfully(200 OK).

Output:

```json
{
  "uuid": "c679f1a7-0a40-4037-9cb7-b0bb7b00836e",
  "name": "Django",
  "link_repo": "https://gitlab.com/turma_node/",
  "demo_time": "08:00:00",
  "created_at": "2022-05-17",
  "instructor": null,
  "students": []
}
```

## PUT /api/courses/<course_id>/registrations/instructor/

This endpoint is to add a instructor to a specific course, it's required to be a admin, the bearer autentication token and the id must be pass in the url. The instructors are only admin users.

Input:

```json
{
  "instructor_id": "5d880acd-cad7-424d-9b23-dffa6aa10372"
}
```

If the request is sucessfully(200 OK).

Output:

```json
{
  "uuid": "c679f1a7-0a40-4037-9cb7-b0bb7b00836e",
  "name": "Node",
  "link_repo": "https://gitlab.com/turma_node/",
  "demo_time": "08:00:00",
  "created_at": "2022-05-17",
  "instructor": {
    "uuid": "5d880acd-cad7-424d-9b23-dffa6aa10372",
    "first_name": "eric",
    "last_name": "martins",
    "email": "eric@bol.com.br",
    "is_admin": true
  },
  "students": []
}
```

## PUT /api/courses/<course_id>/registrations/students/

This endpoint is to add a list of students to a specific course, it's required to be a admin, the bearer autentication token and the id must be pass in the url. The students are only not admin users.

Input:

```json
{
  "students_id": ["cd38010a-4b8d-4257-b160-761ed34bf183"]
}
```

If the request is sucessfully(200 OK).

Output:

```json
{
  "uuid": "dba4ab8b-77a3-4b6e-bc98-05d6e9f6c7dd",
  "name": "Django",
  "link_repo": "https://gitlab.com/turma_node/",
  "demo_time": "08:00:00",
  "created_at": "2022-05-17",
  "instructor": null,
  "students": [
    {
      "uuid": "cd38010a-4b8d-4257-b160-761ed34bf183",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john_doe@bol.com.br",
      "is_admin": false
    }
  ]
}
```

## DELETE /api/courses/<course_id>/

This endpoint is to delete a specific course, it's required to be a admin, the bearer autentication token and the id must be pass in the url.

Input:
Don't need input.

If the request is sucessfully(204 No content).

Output:
Don't have.
