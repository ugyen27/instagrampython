#pip install instaloader
import instaloader
ig = instaloader.Instaloader() # creating instance
dp = input("Enter your id:")
ig.download_profile(dp,profile_pic_only=True)
