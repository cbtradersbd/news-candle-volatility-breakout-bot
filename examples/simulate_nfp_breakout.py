import asyncio
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from src.news.calendar_scraper import EconomicCalendarScraper
from src.strategy.spike_straddle_engine import SpikeStraddleEngine

console = Console()

async def main():
    console.print(Panel("[bold cyan]⚡ NEWS CANDLE VOLATILITY BREAKOUT & STRADDLE ENGINE[/bold cyan]\n"
                        "[green]Official Telegram Channel:[/green] https://t.me/+R_kEsY9yqkA1NDI1\n"
                        "[magenta]Custom Bot Development:[/magenta] @YouKnowWho_am (Telegram)\n"
                        "[yellow]API Endpoint:[/yellow] https://api1.api.cbtradersbd.com/docs",
                        title="High-Impact News Trading Architecture"))
    
    events = EconomicCalendarScraper.get_upcoming_events()
    target_event = events[0]
    console.print(f"[bold yellow]Active Target Event:[/bold yellow] [bold white]{target_event['event']} ({target_event['currency']})[/bold white] | Countdown: [red]15s[/red]")
    
    console.print("[dim]Simulating pre-news freeze and instantaneous post-announcement tick delta...[/dim]\n")
    
    base_price = 1.08450
    engine = SpikeStraddleEngine()
    
    table = Table(title="Live Spike Velocity & Execution")
    table.add_column("Elapsed Time", style="cyan")
    table.add_column("Price", style="bold")
    table.add_column("Delta Pips", justify="right")
    table.add_column("Breakout Signal", style="bold green")
    table.add_column("Broker Action", style="yellow")
    
    ticks = [(0.1, 1.08465), (0.3, 1.08510), (0.5, 1.08585), (1.0, 1.08640)]
    for elapsed, p in ticks:
        res = engine.evaluate_breakout(base_price, p, elapsed)
        table.add_row(
            f"+{elapsed}s",
            f"{p:.5f}",
            f"+{res['delta_pips']} pips",
            f"[bold green]{res['direction']}[/bold green]" if res["is_valid_breakout"] else "[dim]WAITING[/dim]",
            "[bold green]INSTANT ORDER EXECUTED (60s)[/bold green]" if res["is_valid_breakout"] else "[dim]MONITORING[/dim]"
        )
        await asyncio.sleep(0.3)
        
    console.print(table)
    console.print("\n[bold green]✓ Economic news breakout simulation completed successfully![/bold green]")

if __name__ == "__main__":
    asyncio.run(main())
