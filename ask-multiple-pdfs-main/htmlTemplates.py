css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://ww1.freelogovectors.net/wp-content/uploads/2023/09/chatgpt_logo-freelogovectors.net_-640x474.png?lossy=1&ssl=1&fit=640%2C474" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://scontent-waw1-1.xx.fbcdn.net/v/t39.30808-6/228502667_4165452293508275_5710953635627351180_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=a2f6c7&_nc_ohc=_bhSdoXA6K8AX9dxZMm&_nc_ht=scontent-waw1-1.xx&oh=00_AfBtnYzRsUND3-K_B8ih9ZXgUG1aL3hMd_EblRHCn8a_gQ&oe=6508AF12">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
