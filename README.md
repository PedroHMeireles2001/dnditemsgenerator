# Magical Items Generator for D&D

Welcome to the Magical Items Generator, an application powered by Artificial Intelligence to enhance your adventures in the world of Dungeons & Dragons! 🎲✨

## Overview

This application has been developed to provide a unique experience in creating magical items to enrich your D&D campaigns. Using advanced AI algorithms, the generator will produce magical items with detailed descriptions, intriguing stories, and unique properties.

## Key Features

1. **Creative AI:** The AI behind the generator is trained to craft engaging stories and unique concepts for each item, bringing your fantasy world to life.

2. **Open Source:** This project is open to all enchanters and wizards! Contribute, customize, and expand the magical realms by participating in the development of this Open Source initiative.

At this time, the application is not available online due to budget considerations. However, you can download and run the application locally on your machine.


## How to Use

1. Start by ensuring you have Docker and Git installed on your machine.

2. Clone the repository to your local environment.

3. Create a `.env` file inside the `Flask` folder with the necessary environment variables, including your OpenAI API key. If you don't have an API key, follow the steps below to obtain one:

   - Visit the [OpenAI website](https://openai.com/signup/).
   - Sign up for an account or log in if you already have one.
   - Follow the instructions to request access to the OpenAI API.
   - Once approved, navigate to the API section to generate your API key.

4. In your `.env` file, add the OpenAI API key:
   ```dotenv
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the application using Docker Compose with the command `docker-compose up`.

6. Access the web application at `localhost:3000`.

7. Enter an idea for an item into the text field and click the submit button or click the surprise-me buttom to generate a random item


**Note:** If you need additional OpenAI API credits, you can purchase them by visiting the [OpenAI Pricing](https://openai.com/pricing) page on their website. Follow the instructions to buy credits and ensure uninterrupted access to the powerful OpenAI API for magical item generation.

## Contributions

This project is open source! Feel free to contribute, report issues, or suggest new features. Your magic can further enhance this experience for all D&D adventurers.

### How to Contribute

1. Fork the repository.
2. Make your modifications.
3. Open a pull request.
4. Share the magic!

## Troubleshooting

### Port Conflict (3000 or 5000)

**Issue:** If you encounter a port conflict, it might be because another application is already using ports 3000 or 5000.

**Solution:** Ensure that no other applications are using these ports. You can either stop the conflicting application.

### Invalid OpenAI API Key

**Issue:** If you see errors related to an invalid API key, it means your OpenAI API key might be incorrect or expired.

**Solution:** Double-check your `.env` file to ensure the `OPENAI_API_KEY` is correct. If needed, obtain a new API key from the [OpenAI website](https://beta.openai.com/signup/).

### Insufficient OpenAI API Credits

**Issue:** If you encounter errors related to insufficient credits, it means your OpenAI API key doesn't have enough credits.

**Solution:** Verify your credit balance on the [OpenAI Pricing](https://beta.openai.com/pricing) page and replenish credits if necessary.


## License

This project is licensed under the MIT License. Feel free to wield the magic within the terms of this license and embark on your own enchanted adventures!