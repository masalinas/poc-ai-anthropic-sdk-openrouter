import anthropic

client = anthropic.Anthropic(
     api_key="<YOUR_OPENROUTER_API_KEY>",
     base_url="https://openrouter.ai/api"
)

message = client.messages.create(
    #model="anthropic/claude-sonnet-4.5",
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}]
)

print(message.content[0].text)
