This project provides a graphql API endpoint for clients to request specific data about person and address
It's using Django framework.

### Setup and Run
- Clone repo
- `cd graphql_system/`
- Create a virtual env with `python3 -m venv env` and `. env/bin/activate`
- run `pip3 install -r requirements.txt`
- `python manage.py migrate`
- Load some initial data(use any option)
  - option1: `python manage.py loaddata graphql_system/person/fixtures/person_data.json`
  - option2:
    - Create user from terminal `python manage.py createsuperuser`
    - run `python manage.py runserver`
    - go to http://127.0.0.1:8000/admin/
    - Add an Address and Person using the admin panel
- Then run `python manage.py runserver`
- Go to http://127.0.0.1:8000/graphql/ for testing graphql queries

### Sample graphql queries to use:

- Query to display all the persons:

`query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}`

- Query to display a specific person when given an ID:

`query {
  getPerson(id:1) {
    id
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}`

- Create a Person with an Address

`mutation {
  createPerson(
    input:{
        email: "someemail@some.com"
        name: "some name"
        address: {
          number: 99
          street: "Some Street Suburb"
          city: "City"
          state: "ACT"
        }
      } 
)
  {
      person {
        email
        name
        address {
          number
          street
          city
          state
        }
      }
	}
}`

- Update some data of an existing Person

`mutation {
  updatePerson(
    id:4,
    input:{
        email: "ts@some.com"
        name: "ss bb"
        address: {
          number: 77
          street: "Some Street Salisbury"
          city: "Adelaide"
          state: "SA"
        }
      } 
)
  {
    	ok
      person {
        email
        name
        address {
          number
          street
          city
          state
        }
      }
    errors
	}
}`

### Django Tests:

The unit tests are written in folder `graphql_system/person/tests`
More tests could be covered if more time


