import google.generativeai as genai

genai.configure(api_key="AIzaSyDFpSj1F9qrpH0v-oP_4k799otjea1-yTk")

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
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)