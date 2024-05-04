# [AI Home Advisor](https://www.home-ai-advisor.vercel.com/)

This project uses AI to generate personalized real estate recommendations based on your life situation and income. The real estate data is sourced from the Czech Republic site [sreality.cz](https://www.sreality.cz/). The data can be stored in a MongoDB database, populated by a scraper available on [GitHub](https://github.com/karlosmatos/sreality-scraper).

[![AI Home Advisor](./public/screenshot.png)](https://www.home-ai-advisor.vercel.app/)

## How it works

AI Home Advisor uses both [Mixtral](https://mistral.ai/news/mixtral-of-experts/) and [Llama 3](https://llama.meta.com/llama3/) with FastAPI in backend to generate real estate recommendations. The user can input their life situation and income, and the AI will generate a list of real estate recommendations based on the user's input. The AI will then filter the real estate data from sreality.cz and return the filtered data to the user.

## Running Locally

1. Clone the repository with `git clone https://github.com/karlosmatos/home-ai-advisor.git`.
2. Copy the `.env.example` file to `.env`.
3. Create an account at [Groq.com](https://www.groq.com/) and add your API key under `GROQ_API_KEY` in your `.env`
4. Add the base URL of the API under `NEXT_PUBLIC_API_BASE_URL` in your `.env`. If you are running the application locally, it should be `http://localhost:8000`.
5. Install the dependencies with `npm install`.
6. Run the application with `npm run dev` and it will be available at `http://localhost:3000`. API will be available at `http://localhost:8000/docs`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/karlosmatos/home-ai-advisor&env=GROQ_API_KEY,NEXT_PUBLIC_API_BASE_URL&project-name=ai-home-advisor&repo-name=aihomeadvisor)