require('dotenv').config();

// TypeScript
import { LinkedInProfileScraper } from 'linkedin-profile-scraper';

// Plain Javascript
// const { LinkedInProfileScraper } = require('linkedin-profile-scraper')

(async() => {
  const scraper = new LinkedInProfileScraper({
    sessionCookieValue: 'AQEDATVKaoMCosrcAAABfpdEylMAAAF-u1FOU1YAcW964ZGaHKx5wVmK6fFSd-XfXeYdMwVVIAJ01CLCbgp9HyVW4sGGlGfVOXllOMmWDC67NQb_R5RG4JvF4lLY4XTbDY1jo8W8IO-Ks7tBVfh0UKN2',
    keepAlive: false
  });

  // Prepare the scraper
  // Loading it in memory
  await scraper.setup()

  const result = await scraper.run('https://www.linkedin.com/in/jvandenaardweg/')

  console.log(result)
})()