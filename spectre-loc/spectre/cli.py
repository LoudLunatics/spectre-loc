def main():
    show_welcome()
    
    # Input target sekarang berupa IP atau Range
    target = console.input("[bold red]SPECTRE[/bold red]@[bold white]target_ip/range[/bold white]: ")
    
    # Fitur baru: Pilih Mode
    mode = console.input("[bold red]SPECTRE[/bold red]@[bold white]stealth_mode(y/n)[/bold white]: ").lower()
    is_stealth = True if mode == 'y' else False

    show_status(f"Scanning target {target} in {'GHOST' if is_stealth else 'NORMAL'} mode...")

    engine = SpectreEngine()
    
    # Proses Scan
    with console.status("[bold yellow]Infiltrating network...[/bold yellow]"):
        results = engine.search_radar(target, stealth_mode=is_stealth)

    # ... (Tampilkan hasil dengan Table seperti sebelumnya)
