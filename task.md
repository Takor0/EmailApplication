# The Software House recruitment task

The repository contains solution for [TSH](https://tsh.io/) recruitment task. The description of the task is available in [task.md](./task.md).

## Used technologies

The project is written in [TypeScript](https://www.typescriptlang.org/) and uses [Node.js](https://nodejs.org/), [Express](https://expressjs.com/), [Jest](https://jestjs.io/) and [Yarn](https://yarnpkg.com/).

## Requirements

The project requires `Node.js` and `Yarn` to be installed in the runtime environment. The project was developed in environment with packages in versions:

- `Node.js v12.16.2`
- `Yarn 1.22.4`

`Yarn` requires version 1.x installed in the environment but actually it uses version 2.x which is installed in the project. See `Yarn`'s [installation page](https://yarnpkg.com/getting-started/install#per-project-install) for details.


## Run instructions

### Install

The project follows [`Zero-Installs`](https://yarnpkg.com/features/zero-installs) pattern so there is no need to install any packages.

### Build

To build the project run command from project's main folder:

```shell
yarn build
```

### Start

Before start the project must be built. To start the project run command from project's main folder:

```shell
yarn start
```

### Unit Tests

To run tests run command from project's main folder:

```shell
yarn test
```

## Implementation details

Application provides REST API to add Movie and retrieve Movies and Genres. There are available three endpoints:

### `GET /api/genres`

Returns list of all available Genres

### `GET /api/movies`

Returns collection of the movies according to task requirements. Two filters (`duration`, `genres`) are available which must be passed as a query string. Example:

`http://localhost:3000/api/movies?duration=100&genres[]=Animation&genres[]=Adventure&genres[]=Comedy`

### `POST /api/movies`

Endpoint for adding new Movie to the storage. The request body should contain proper JSON. Example:

```json
{
  "title": "Title",
  "year": 2005,
  "runtime": 200,
  "genres": [
    "Music",
    "Family",
    "Comedy"
  ],
  "director": "Director",
  "actors": "Actor 1, Actor 2",
  "plot": "Lorem ipsum",
  "posterUrl": "http://example.com/posters/movie1.jpg"
}
```

## Additional info

The repository contains [Postman](https://www.postman.com/) Collection available in [TSH.postman_collection.json](./TSH.postman_collection.json).
