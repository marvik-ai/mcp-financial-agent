from agents import (HandoffOutputItem, ItemHelpers, MessageOutputItem,
                    Runner, ToolCallItem, ToolCallOutputItem, trace)


async def process_user_input(agent, input_items, user_input, conversation_id):
    """Process user input and return the agent's response."""
    with trace("Customer service", group_id=conversation_id):
        input_items.append({"content": user_input, "role": "user"})

        # Run the agent with the current conversation context
        result = await Runner.run(agent, input_items, context={})

        # Process the agent's response
        responses = []
        for new_item in result.new_items:
            agent_name = new_item.agent.name
            if isinstance(new_item, MessageOutputItem):
                responses.append(f"{agent_name}: {ItemHelpers.text_message_output(new_item)}")
            elif isinstance(new_item, HandoffOutputItem):
                responses.append(
                    f"Handed off from {new_item.source_agent.name} to {new_item.target_agent.name}"
                )
            elif isinstance(new_item, ToolCallItem):
                responses.append(f"{agent_name}: Calling tool {new_item.raw_item}")
            elif isinstance(new_item, ToolCallOutputItem):
                responses.append(f"{agent_name}: Tool call output: {new_item.output}")
            else:
                responses.append(f"{agent_name}: Skipping item: {new_item.__class__.__name__}")

        # Update conversation memory and agent state
        input_items = result.to_input_list()
        return responses, input_items, result.last_agent
 

def format_response(responses):
    """Format the agent's responses for display."""
    formatted_responses = []
    for response in responses:
        if isinstance(response, MessageOutputItem):
            formatted_responses.append(f"Assistant: {ItemHelpers.text_message_output(response)}")
        elif isinstance(response, HandoffOutputItem):
            formatted_responses.append(
                f"Handed off from {response.source_agent.name} to {response.target_agent.name}"
            )
        elif isinstance(response, ToolCallItem):
            formatted_responses.append(f"Calling tool {response.raw_item}")
        elif isinstance(response, ToolCallOutputItem):
            formatted_responses.append(f"Tool call output: {response.output}")
        else:
            formatted_responses.append(f"Skipping item: {response.__class__.__name__}")
    return formatted_responses


async def console_chat(agent):
    """Console-based chat interface."""
    input_items = []

    while True:
        # Get user input

        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the conversation. Goodbye!")
            break

        input_items.append({"content": user_input, "role": "user"})
        run_result = await Runner.run(
            agent,
            input_items,
            context={},
        )
        # Process the user input
        messages = format_response(run_result.new_items)

        input_items = run_result.to_input_list()
        
        # Display the agent's responses
        for message in messages:
            print(message)
