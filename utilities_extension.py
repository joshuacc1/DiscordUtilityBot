import os
import re
import time
from discord.ext import commands #, tasks
import discord
#from discord import File, Embed, Color

from store.links import add_links, get_links

# Define a custom modal for user input
class MyModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Fill in your parameters")

        # Add text input fields to the modal
        self.name = discord.ui.TextInput(
            label="Name", 
            placeholder="Enter your name",
            max_length=100
        )
        self.age = discord.ui.TextInput(
            label="Age", 
            placeholder="Enter your age", 
            style=discord.TextStyle.short
        )
        self.occupation = discord.ui.TextInput(
            label="Occupation",
            placeholder="Enter your occupation",
            style=discord.TextStyle.paragraph
        )

        # Add fields to the modal
        self.add_item(self.name)
        self.add_item(self.age)
        self.add_item(self.occupation)

    # Handle submission of the modal
    async def on_submit(self, interaction: discord.Interaction):
        # Send the user's input back as a response
        await interaction.response.send_message(
            f"Name: {self.name.value}\nAge: {self.age.value}\nOccupation: {self.occupation.value}"
        )



class Utilities_extension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="save_link", description="An example command with prefillable fields")
    async def example(self, interaction: discord.Interaction, link: str, description: str = ""):
        """
        A slash command that accepts arguments directly in the command input box.
        """
        add_links(interaction.user.name, link, description)
        response = (
            "Added the following link to the database:\n"
            f"Link: {link}\n"
            f"Description: {description}\n"
        )
        await interaction.response.send_message(response)

    @discord.app_commands.command(name="subscribe", description="Open a modal to fill in parameters")
    async def subscribe(self, interaction: discord.Interaction):
        modal = MyModal()
        await interaction.response.send_modal(modal)

    @commands.group(name="links")
    async def links(self,ctx: commands.Context):
        await ctx.send(f'links group executed')

    @links.command(name="add")
    async def add(self,ctx: commands.Context, link: str, description: str):
        print(f"added link {link} {description}")
        add_links(ctx.author.name, link, description)
        await ctx.send(f'Added link {link} with description {description}')
    
    @links.command(name="get")
    async def get(self, ctx: commands.Context, author: str = None):
        links = get_links()
        for link in links:
            if author:
                if link["author"] == author:
                    await ctx.send(f'{link["author"]} {link["link"]} {link["description"]}')
            else:
                await ctx.send(f'{link["author"]} {link["link"]} {link["description"]}')


async def setup(bot: commands.Bot):
    print("setting up utilitiescog")
    await bot.add_cog(Utilities_extension(bot))