import os
import subprocess


def main():
    pass

def limpiar():
    """Limpia la terminal de forma segura en Windows, Linux y macOS."""
    if os.name == "nt":
            # Windows necesita shell=True porque 'cls' es un comando interno
            # de la consola.
            subprocess.run("cls", shell=True)
    else:
            # Linux y macOS ejecutan 'clear' directamente.
            subprocess.run(["clear"])


def pausar():
    input("\n\nPulsa <ENTER> para continuar...")

if __name__ == "__main__":
    main()