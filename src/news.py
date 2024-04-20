import google.generativeai as genai

genai.configure(api_key="apikey")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Note I will give my origin and destination so u have provide me new related my route"]
  },
  {
    "role": "model",
    "parts": ["Sounds good! Just let me know your origin and destination, and I'll provide you with some new route options related to your original path. I'm excited to help you explore! 🗺️🚗"]
  },
  {
    "role": "user",
    "parts": ["India to singapur"]
  },
  {
    "role": "model",
    "parts": ["## India to Singapore: Exploring New Routes 🇮🇳✈️🇸🇬 \n\nWhile the most common way to travel between India and Singapore is by air, there are indeed alternative routes and methods to consider, each offering a unique experience. Let's explore some options:\n\n*By Air (with a twist):\n\n *Multi-city flights:* Instead of a direct flight, consider a multi-city option with layovers in interesting locations like Bangkok, Kuala Lumpur, or Ho Chi Minh City. This allows you to explore another city on your way to Singapore. \n* *Budget airlines:* Explore airlines like AirAsia, Scoot, or IndiGo for potentially cheaper fares, especially if you're flexible with your travel dates and times. \n* *Luxury airlines:* For a more luxurious experience, consider airlines like Singapore Airlines or Emirates, renowned for their excellent service and comfort.\n\n*By Sea:\n\n *Cruise ships:*  Several cruise lines offer routes that include both India and Singapore. This option allows you to enjoy a relaxing journey with onboard amenities and visit multiple destinations along the way. \n* *Cargo ship voyages:* For the truly adventurous, consider a cargo ship voyage. This is a unique and economical way to travel, offering a glimpse into the world of maritime transport. \n\n*Overland (the ultimate adventure):\n\n *India-Myanmar-Thailand-Malaysia-Singapore:* This overland route involves a combination of buses, trains, and possibly even ferries. It's a long and challenging journey, but it offers an incredible opportunity to experience the diverse cultures and landscapes of Southeast Asia. \n* *India-Nepal-Tibet-China-Southeast Asia:*  This route takes you through the Himalayas and offers breathtaking scenery. However, it requires careful planning and may involve obtaining special permits for certain regions. \n\n*Things to Consider:\n\n *Budget:* Air travel is generally the fastest but can be more expensive, while overland travel is the most budget-friendly but time-consuming.\n* *Time:*  Consider how much time you have for your journey and choose the option that fits your schedule.\n* *Interests:* Choose a route that aligns"]
  },
  {
    "role": "user",
    "parts": ["u just have to provide me sea route new related to origin and destination"]
  },
  {
    "role": "model",
    "parts": ["My apologies for the broader options! Let's focus on new and exciting sea routes from India to Singapore: \n\n## Sea Routes from India to Singapore: Charting New Waters 🇮🇳🚢🇸🇬\n\nWhile direct cargo ship voyages between India and Singapore might be limited,  we can explore some creative sea route options by incorporating cruises and ferries, offering a mix of adventure and luxury:\n\n*Cruise options:\n\n *Cruises from Mumbai/Chennai with stops in Southeast Asia:* Several major cruise lines offer itineraries starting from Indian ports like Mumbai or Chennai, making stops at various Southeast Asian destinations like Phuket, Penang, and Port Klang (gateway to Kuala Lumpur) before reaching Singapore. This allows you to experience the diverse cultures and landscapes of the region while enjoying the comfort and amenities of a cruise ship.\n* *Luxury cruises from Singapore with stops in Indian ports:*  Another option is to start your journey from Singapore and embark on a luxury cruise that includes stops at Indian ports like Cochin, Goa, or Mumbai. This way, you can experience the vibrant culture and historical sites of India before concluding your trip in Singapore.\n* *Repositioning cruises:* Keep an eye out for repositioning cruises, where cruise ships move between regions during seasonal changes. These cruises often offer unique itineraries with stops at less-visited ports, potentially including routes between India and Southeast Asia.\n\n*Ferry options:\n\n *Island hopping in the Andaman Sea:*  This option is perfect for those seeking adventure and island exploration. Start your journey from the Andaman and Nicobar Islands, a union territory of India, and hop on ferries to various islands in the Andaman Sea, including those belonging to Thailand and Myanmar, before eventually reaching mainland Malaysia. From there, you can take a bus or train to Singapore.\n* *Ferry connections from Indonesian islands:* Explore the possibility of ferry connections from Indonesian islands like Batam or Bintan, which are relatively close to Singapore, to ports in the Andaman and Nicobar Islands or mainland India. This option allows you to experience the beauty of Indonesia's islands and combine it with a sea voyage to India.\n\n*Additional considerations:\n\n *Visa requirements:* Research and ensure you have the necessary visas for all countries you plan to visit or transit through during your sea voyage.\n* *Ferry schedules and connections:*  Ferry schedules and routes can be subject to change, so it's essential to research and plan your connections in advance.\n* *Travel time:* Sea voyages can be time-consuming, so factor in the travel time when planning your journey. \n* *Costs:* Compare the costs of different cruise lines and ferry options to find one that fits your budget."]
  },
  {
    "role": "user",
    "parts": ["Note u just have to provide realted to route and that should be negetive if have like war , wheather conditoin etc"]
  },
  {
    "role": "model",
    "parts": ["My apologies for not focusing on the potential downsides earlier. Let's delve into some of the challenges and negative aspects you might encounter on these sea routes:\n\n## Challenges and Negatives of Sea Routes from India to Singapore: 🇮🇳🚢🇸🇬\n\n*Weather conditions:\n\n *Monsoon season:* The monsoon season in the Indian Ocean, typically between June and September, can bring heavy rains, strong winds, and rough seas, making sea travel challenging and potentially dangerous. \n* *Typhoons and cyclones:* The Southeast Asian region, including the South China Sea, is prone to typhoons and cyclones, especially between July and November. These storms can disrupt shipping schedules and pose safety risks.\n\n*Piracy concerns:\n\n *Straits of Malacca and Singapore:* Although piracy has declined in recent years, the Straits of Malacca and Singapore have historically been areas of concern.  While cruise ships and larger vessels are generally safe, smaller boats and yachts may be more vulnerable.\n\n*Geopolitical factors:\n\n *Territorial disputes in the South China Sea:* Ongoing territorial disputes in the South China Sea between several countries, including China, Vietnam, and the Philippines, could potentially lead to tensions and affect shipping routes.\n* *Political instability in neighboring countries:* Political instability or unrest in neighboring countries like Myanmar or Thailand could potentially impact travel plans and border crossings.\n\n*Other challenges:\n\n *Seasickness:*  If you're prone to seasickness, prolonged sea travel can be uncomfortable and unpleasant.\n* *Limited connectivity:* Depending on the vessel and route, internet and phone connectivity may be limited or expensive on board.\n* *Environmental impact:* Cruise ships can have a significant environmental impact, contributing to air and water pollution. Consider choosing eco-friendly cruise lines or alternative travel options with a lower carbon footprint.\n\n*Additional factors to research:\n\n *Specific risks in certain areas:*  Research the specific risks associated with the regions you plan to travel through, such as areas known for piracy or political instability.\n* *Travel advisories:* Check for any travel advisories or warnings issued by your government or relevant authorities regarding the countries you plan to visit.\n\n*Remember, careful planning and research are crucial to mitigate risks and ensure a safe and enjoyable journey.*"]
  },
  {
    "role": "user",
    "parts": ["Just give me usefull news related to my route and do not return other thing's"]
  },
  {
    "role": "model",
    "parts": ["## Useful News for Your India to Singapore Sea Route: 🇮🇳🚢🇸🇬\n\n* *Monsoon season updates:* Stay informed about the current monsoon conditions and forecasts, especially if traveling between June and September. This will help you avoid rough seas and potential disruptions to your journey.\n* *Typhoon and cyclone warnings:*  Monitor weather reports for any typhoon or cyclone activity in the region, particularly between July and November. This is crucial for planning your trip and ensuring your safety at sea.\n* *Piracy reports and safety advisories:* Check for any recent piracy incidents or safety advisories issued for the Straits of Malacca and Singapore. While the risk is generally low, staying informed helps you make informed decisions about your route and vessel choice. \n* *Geopolitical developments:* Stay updated on any geopolitical developments or tensions in the South China Sea and surrounding regions. This could impact shipping routes and border crossings.\n* *Cruise line and ferry updates:* Keep track of any changes or disruptions to cruise schedules or ferry routes, especially during the monsoon season or due to unforeseen events.\n* *Port closures or restrictions:*  Monitor news for any port closures or restrictions that may affect your itinerary, such as those related to political unrest or health concerns.\n* *Travel advisories and visa requirements:* Stay informed about the latest travel advisories and visa requirements for all countries you plan to visit or transit through during your sea voyage.\n* *Sustainable travel options:* Research eco-friendly cruise lines or responsible ferry operators to minimize the environmental impact of your journey."]
  },
  {
    "role": "user",
    "parts": ["Russia to ukrain"]
  },
  {
    "role": "model",
    "parts": ["## Russia to Ukraine: Navigating a Complex Situation \n\n*Due to the ongoing conflict, travel between Russia and Ukraine is currently highly restricted and unsafe.  *\n\nHere's what you need to know:\n\n*Travel Restrictions:\n\n *Border closures:* The land border between Russia and Ukraine is largely closed, with limited exceptions for humanitarian aid and specific authorized crossings.\n* *Flight restrictions:* Direct flights between Russia and Ukraine are suspended. \n* *Visa limitations:* Obtaining visas for travel between the two countries is extremely difficult due to the current political situation.\n\n*Safety Concerns:\n\n *Active conflict zones:*  Active fighting and shelling continue in various regions of Ukraine, posing significant risks to personal safety.\n* *Landmines and unexploded ordnance:*  Many areas are contaminated with landmines and unexploded ordnance, making travel by land dangerous. \n* *Military checkpoints and security measures:* Expect strict security measures, including military checkpoints and potential questioning or detention.\n\n*Alternative Routes:\n\n *Travel through neighboring countries:*  It may be possible to travel between Russia and Ukraine via neighboring countries like Belarus, Poland, or Moldova, depending on current border restrictions and visa requirements. However, this can be a complex and time-consuming process.\n\n*Essential Resources:\n\n *Government travel advisories:*  Consult travel advisories issued by your government and relevant authorities for the latest information on safety risks and travel restrictions.\n* *International organizations:* Organizations like the United Nations and the International Committee of the Red Cross may provide updates on the humanitarian situation and potential travel corridors.\n* *News outlets:* Stay informed about the latest developments in the conflict through reputable news sources. \n\n*It is strongly advised to avoid all travel to Ukraine at this time due to the ongoing conflict and significant safety risks.*"]
  },
  {
    "role": "user",
    "parts": ["perfect"]
  },
  {
    "role": "model",
    "parts": ["I'm glad the information was helpful. Please remember that the situation in the region is constantly evolving, so it's crucial to stay updated with the latest news and travel advisories before making any travel decisions. Stay safe!"]
  },
  {
    "role": "user",
    "parts": ["india to pakisthan"]
  },
  {
    "role": "model",
    "parts": ["## India to Pakistan: A Journey with Hurdles 🇮🇳 🇵🇰\n\nTraveling between India and Pakistan presents unique challenges due to the complex political relationship between the two countries. While it's not impossible, it requires careful planning and awareness of the limitations.\n\n*Travel Restrictions:\n\n *Limited border crossings:*  The only land border crossing open for foreigners is the Wagah-Attari border near Amritsar, India, and Lahore, Pakistan. \n* *Visa requirements:* Obtaining a visa can be a lengthy and complex process, often requiring extensive documentation and a clear purpose for travel. Tourist visas are generally difficult to obtain.\n* *Restricted areas:* Certain areas near the border and in Kashmir may be off-limits to foreigners or require special permits. \n\n*Transportation Options:\n\n *Flights:* Limited direct flights operate between major cities like Delhi and Mumbai in India and Lahore and Karachi in Pakistan. Indirect flights with layovers in other countries are also available. \n* *Bus:*  A bus service operates between Delhi and Lahore, crossing the Wagah-Attari border.\n* *Train:* The Samjhauta Express train service between Delhi and Lahore has been suspended indefinitely. \n\n*Things to Consider:\n\n *Political climate:* The political situation between India and Pakistan can be unpredictable, with occasional tensions and border closures. It's crucial to stay updated on current events and be prepared for potential disruptions. \n* *Security concerns:* Security measures are generally tight at border crossings and in major cities. Be prepared for thorough checks and questioning. \n* *Cultural sensitivity:*  Respect local customs and traditions, dress modestly, and be mindful of cultural sensitivities.\n\n*Essential Resources:\n\n *Government websites:* Consult the official websites of the Indian and Pakistani governments for the latest visa information and travel advisories.\n* *Travel agencies:* Specialized travel agencies can assist with visa applications, travel arrangements, and provide guidance on navigating the complexities of travel between the two countries.\n* *News sources:* Stay informed about the current political climate and security situation through reputable news sources.\n\n*Traveling between India and Pakistan requires patience, flexibility, and a willingness to navigate bureaucratic hurdles. It's essential to plan well in advance and be prepared for potential challenges.*"]
  },
])

convo.send_message("India to russia")
print(convo.last.text)