import rich
from google.cloud.pubsub_v1.types import Subscription, Topic
from rich.panel import Panel


class Printer:
    @staticmethod
    def print_error(error: Exception) -> None:
        """
        Prints a red panel with the error message.

        Args:
            error (Exception): The error to print.
        """
        content = f"\n[bold red]{type(error).__name__}:[/bold red] [white]{error}\n"
        panel = Panel.fit(content, border_style="red", title="Error", title_align="left")
        rich.print(panel)

    @classmethod
    def print_topic(cls, topic: Topic) -> None:
        """
        Prints a Topic in a colored panel.

        Args:
            topic (Topic): The topic to print.
        """
        id_ = topic.name.split("/")[-1]
        content = cls._color_dictionary(Topic.to_dict(topic))
        panel = Panel(content, title=f"[TOPIC]: {id_}", border_style="white", title_align="left")
        rich.print("\n", panel)

    @classmethod
    def print_subscription(cls, subscription: Subscription) -> None:
        """
        Prints a Subscription in a colored panel.

        Args:
            subscription (Subscription): The subscription to print.
        """
        id_ = subscription.name.split("/")[-1]
        content = cls._color_dictionary(Subscription.to_dict(subscription))
        panel = Panel(content, title=f"[SUBSCRIPTION]: {id_}", border_style="white", title_align="left")
        rich.print("\n", panel)

    @staticmethod
    def _color_dictionary(dictionary: dict) -> rich.text.Text:
        """
        Colors the keys and values of a dictionary.

        Args:
            dictionary (dict): The dictionary to color.

        Returns:
            str: The colored dictionary as a string.
        """
        content = rich.text.Text()
        content.append("\n")

        for key, value in dictionary.items():
            content.append(rich.text.Text(str(key), style="bold cyan"))
            content.append(": ")
            content.append(rich.text.Text(str(value), style="magenta"))
            content.append("\n")

        return content
