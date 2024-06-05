# Advance API

API Usage Guide
How to Read API Documentation to Find the Endpoints You’re Looking For
API documentation is designed to help developers understand how to interact with an API. Here's a step-by-step guide:

1. Understand the API Structure
Base URL: The root address for accessing the API.
Endpoints: Specific paths you append to the base URL to access different functionalities.
2. Explore the Sections
Introduction: Provides an overview of the API.
Authentication: Details on how to authenticate with the API (e.g., API keys, OAuth).
Endpoints: Lists all available endpoints. Usually organized by resources (e.g., /users, /posts).
3. Look for Endpoint Details
HTTP Methods: Indicates the type of request (GET, POST, PUT, DELETE).
Parameters: Includes path parameters, query parameters, and request body details.
Responses: Example responses, including status codes and data structures.
4. Examples
Documentation often includes example requests and responses to illustrate usage.
How to Use an API with Pagination
Pagination is used to split large datasets into smaller chunks. Here’s how to handle it:

1. Identify Pagination Parameters
Common parameters: page, limit, offset, per_page.
2. Make the Initial Request
Request the first page of data using the relevant parameters.
3. Parse the Response
Look for metadata that indicates the total number of pages or items (e.g., total_pages, total_items).
4. Iterate Through Pages
Use a loop to make subsequent requests for each page until you have retrieved all data.
```
async function fetchPaginatedData(apiUrl) {
  let page = 1;
  let results = [];
  let hasMorePages = true;

  while (hasMorePages) {
    const response = await fetch(`${apiUrl}?page=${page}`);
    const data = await response.json();
    results = results.concat(data.items);

    if (page >= data.total_pages) {
      hasMorePages = false;
    } else {
      page++;
    }
  }

  return results;
}
```

### How to Parse JSON Results from an API
1. Fetch the Data
Use fetch or a similar method to make the API call.
2. Parse the JSON
Use .json() to convert the response to a JavaScript object.
```
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => console.error('Error:', error));
```

### How to Make a Recursive API Call
Recursion can be useful for handling paginated APIs. Here’s an example of a recursive function to fetch all pages:

```
async function fetchAllPages(apiUrl, page = 1, results = []) {
  const response = await fetch(`${apiUrl}?page=${page}`);
  const data = await response.json();
  results = results.concat(data.items);

  if (data.has_more_pages) {
    return fetchAllPages(apiUrl, page + 1, results);
  } else {
    return results;
  }
}

fetchAllPages('https://api.example.com/data').then(allData => {
  console.log(allData);
});
```

### How to Sort a Dictionary by Value
Sorting a dictionary (object in JavaScript) by its values can be done by converting it to an array of key-value pairs, sorting it, and then converting it back.

```
const dict = {
  'a': 3,
  'b': 1,
  'c': 2
};

const sortedDict = Object.fromEntries(
  Object.entries(dict).sort(([, a], [, b]) => a - b)
);

console.log(sortedDict); // { b: 1, c: 2, a: 3 }
```
