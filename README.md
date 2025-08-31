# The Koepkes Website

A professional website showcasing Orion and Nicole Koepke's careers and accomplishments, hosted at [koepkes.us](https://koepkes.us).

## Overview

This project is a static website built with HTML, CSS, and JavaScript, developed with the assistance of AI tools including the Cursor IDE and the Claude language model. The site is hosted on AWS S3 and features:

- Responsive design that works on all devices
- Individual portfolio pages for each family member
- Animated transitions and modern UI elements
- Subdomain routing (orion.koepkes.us, nicole.koepkes.us)

## Project Structure 
```
├── bin/
│ └── ctl.py # Control script for project operations
├── src/
│ ├── assets/ # Images and other static assets
│ ├── css/ # Common Stylesheets
│ ├── js/ # Common JavaScript files
│ ├── orion/ # Orion's portfolio page
│ ├── nicole/ # Nicole's portfolio page
│ └── index.html # Main landing page
```

## Project Control

The project includes a control script at `bin/ctl.py` that handles various operations:

### Start the local development server
```
./bin/ctl.py run
```

### Deploy the site to AWS S3
```
./bin/ctl.py deploy
```

## Hosting

The website is hosted on AWS S3 with static website hosting enabled. The domain koepkes.us is configured to point to the S3 bucket through Route 53.

## Development

1. Clone the repository
2. Install Python
3. Install the AWS CLI and set up credentials
    - Follow the [AWS CLI configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) to set up credentials
4. Run `./bin/ctl.py run` to start the local development server
5. Make changes in the `src/` directory
6. Deploy using `./bin/ctl.py deploy`

## Credits

- Development: Orion Koepke
- AI Assistance: Cursor IDE and Claude
- Hosting: AWS S3