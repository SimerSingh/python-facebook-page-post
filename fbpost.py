import facebook

page_access_token = "<Your-facebook-page-access-token-here>"
facebook_page_id = "<Your-facebook-page-id>"
message="<Your-message-to-post-on-page>"

graph = facebook.GraphAPI(page_access_token)

graph.put_object(facebook_page_id, "feed", message=final_post)

print(f"Message {message} posted on your facebook page successfully")

