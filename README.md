This project provides a graphql API endpoint for clients to request specific data about person and address
It's using Django framework.

### Setup and Run
- Clone repo
- `cd graphql_system/`
- Create a virtual env with `python3 -m venv env` and `. env/bin/activate`
- run `pip3 install -r requirements.txt`
- `python manage.py migrate`
- Load some initial data
  - `python manage.py loaddata graphql_system/person/fixtures/person_data.json`
- Then run `python manage.py runserver`
- Go to http://127.0.0.1:8000/graphql/ for testing graphql queries

### Sample graphql queries to use:

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


