from pynput import mouse, keyboard
from ctypes import windll
from pynput.keyboard import Key, Controller
from sys import stdout, exit
from asyncio import sleep as asyncsleep, create_task, run as asyncrun, get_event_loop, gather
from subprocess import run, Popen
from time import sleep
from socket import gethostname, gethostbyname
from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
from os import listdir, stat, path, walk, makedirs, getenv
from random import uniform
from win32con import SW_HIDE
from playsound import playsound
from win32gui import GetForegroundWindow, ShowWindow
from win32gui import SetWindowPos, ShowWindow
from win32con import HWND_TOPMOST, SWP_NOMOVE, SWP_NOSIZE, SW_SHOW, HWND_NOTOPMOST
from psutil import Process, process_iter
from shutil import copytree
from colorama import just_fix_windows_console, Style, Fore
from traceback import print_exc

# Obtém o identificador do terminal e remove os botões de controle
terminal_handle = GetForegroundWindow()
style = windll.user32.GetWindowLongA(terminal_handle, -16)
style &= ~0x00080000  # Remove o botão de minimizar
style &= ~0x00020000  # Remove o botão de restaurar
style &= ~0x00010000  # Remove o botão de fechar
windll.user32.SetWindowLongA(terminal_handle, -16, style)


# Arruma o texto colorido no console
just_fix_windows_console()

# Verifica se está no modo Administrador
def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False

# Caminho para a pasta do executável
base_path = path.dirname(path.abspath(__file__))


def admin():
    
    
    # Pergunta se realmente é desejado entrar no modo Administrador

    print(Style.BRIGHT + Fore.RED + "\033[?25lAre you sure you want to continue? Permanent modifications may occur and the false will become true." + Fore.WHITE + Style.NORMAL)
    playsound(path.join(base_path, "Components", "confirmation.mp3"))
    response = input('\033[?25h')

    while True:
        # Se a resposta for 'yes', o programa iniciará no modo Administrador 
        if response.lower() == 'yes':
            sleep(0.7)
            print(Fore.YELLOW + "\033[?25lYou made your choice, now you are at your own risk..." + Style.RESET_ALL)
            playsound(path.join(base_path, "Components", "you made your choice.mp3"))
            sleep(2)
            run('cls', shell=True)
            break
        # Se a resposta for 'no', o programa fechará
        elif response.lower() == 'no':
            sleep(0.7)
            print(Style.BRIGHT + Fore.WHITE + "\033[?25lYou made the right choice.")
            playsound(path.join(base_path, "Components", "right choice.mp3"))
            sleep(2)
            exit()
        # Se a resposta não for 'yes' ou 'no', dirá o escopo de resposta, e perguntará novamente
        else:
            print(Style.BRIGHT + "\033[?25lPlease answer (yes/no)" + Style.RESET_ALL)
            playsound(path.join(base_path, "Components", "yes or no.mp3"))
            response = input('\033[?25h')
if is_admin():
    admin()

try:
    # Desativa o cursor e o move para o canto direito da tela (alterar)
    mouse_listener = mouse.Listener(suppress=True)
    mouse_listener.start()
    # Define as constantes para os lados direito e inferior da tela
    SM_CXSCREEN = 0
    SM_CYSCREEN = 1
    # Obtém a largura e altura da tela
    width = windll.user32.GetSystemMetrics(SM_CXSCREEN)
    height = windll.user32.GetSystemMetrics(SM_CYSCREEN)
    # Move o cursor para o centro inferior da tela
    windll.user32.SetCursorPos(width, height)

    # Oculta o cursor do terminal
    print('\033[?25l', end="")

    # Define a janela como sempre no topo
    terminal_window = GetForegroundWindow()
    SetWindowPos(terminal_window, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    ShowWindow(terminal_window, SW_SHOW)

    # Deixa o CMD em tela cheia
    keyboardinput = Controller()
    keyboardinput.press(Key.alt)
    keyboardinput.press(Key.enter)
    keyboardinput.release(Key.alt)
    keyboardinput.release(Key.enter)

    # Bloqueia o teclado (alterar)
    keyboard_listener = keyboard.Listener(suppress=True)
    keyboard_listener.start()

    async def loading_animation(duration=3.7, animation_text="Loading...", complement="", clean=False):
        chars = "/—\\|"
        chars_n = " "
        num_iterations = int(duration / (len(chars) * 0.1))

        for _ in range(num_iterations):
            for char in chars:
                stdout.write('\r' + animation_text + ' ' + complement + ' ' + char)
                stdout.flush()
                await asyncsleep(0.1)

        stdout.write('\r' + ' ' * (len(animation_text) + len(chars) + 1))
        # Substituir os chars por chars_n
        stdout.write('\r'  + animation_text + ' ' + complement + ' ' + chars_n * len(chars))
        stdout.flush()

        if clean:
            stdout.write('\r' + ' ' * (len(animation_text) + len (complement) + len(chars) + 1) + '\r')
        else:
            stdout.write('\n')

        stdout.flush()


    async def main():
        # Iniciar a animação em segundo plano
        task = create_task(loading_animation(6, 'Starting NecroCode Nemesis...'))

        
        await asyncsleep(1.5)

        run('color a', shell=True)


        # Espere até que a animação seja concluída
        await task

    if __name__ == "__main__":
        asyncrun(main())
    print("Initialization complete")


    sleep(1.7)
    print("\n" + Style.BRIGHT + "DON'T TURN OFF, ALL YOUR FILES ARE ENCRYPTED\n")

    run('color a', shell=True)
    sleep(3)

    asyncrun(loading_animation(6, 'Disabling firewall and starting port forwarding...'))

    sleep(2)

    run('ipconfig', shell=True)
    sleep(2.5)

    destname = "Black-Hole"
    hostname = gethostname()

    # Obtém o endereço IP associado ao nome da máquina
    destip_address = "192.168.7.5"
    ip_address = gethostbyname(hostname)

    # Crie a string com as informações desejadas
    print(f"\nEstablishing connection from {ip_address} ({hostname}) to {destip_address} ({destname})", end='')

    # Adicione a animação de pontos
    for _ in range(14):  # Altere o número de repetições conforme necessário
        stdout.write('.')
        stdout.flush()
        sleep(0.5)  # Ajuste o atraso (em segundos) conforme necessário

    print("\nConnection established successfully")
    sleep(1.3)
    print("Remote connection allowed\n\n")

    sleep(3.3)


    def find_special_folder(folder_name):
            with OpenKey(HKEY_CURRENT_USER,
                                fr"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as key:
                folder_path = QueryValueEx(key, folder_name)[0]
            return folder_path


    special_folders = {
        "Documents": "Personal",
        "My Video": "My Video",
        "My Picture": "My Pictures",
        "Desktop": "Desktop"
    }

    folder_path_list = []
    for folder_name, reg_name in special_folders.items():
        folder_path = find_special_folder(reg_name)
        if folder_path:
            folder_path_list.append(folder_path)



    async def personal_files_list(folders, duration):
        files_value = 0

        for pasta, folder_name in zip(folders, special_folders.keys()):
            await loading_animation(duration, "Searching for files in", folder_name, clean=True)
            itens = [item for item in listdir(pasta) if not stat(path.join(pasta, item)).st_file_attributes & 2]
            
            if pasta == folder_path_list[3]:  # Área de Trabalho
                itens.append("Pornô Gay com furrys +18 (795.4 GB)")
            
            print(f"{pasta}:")
            for item in itens:
                item_path = path.join(pasta, item)
                tamanho = path.getsize(item_path) if path.isfile(item_path) else get_size_of_folder(item_path)
                
                if item != "Pornô Gay com furrys +18 (795.4 GB)":
                    tamanho_formatado = format_size(tamanho)
                    print(f"    {item} ({tamanho_formatado})")
                    files_value += tamanho
                else:
                    print(f"    {item}")
            
            print()
        
        return files_value



    def get_size_of_folder(folder):
        total_size = 0
        for dirpath, dirnames, filenames in walk(folder):
            for f in filenames:
                fp = path.join(dirpath, f)
                total_size += path.getsize(fp)
        return total_size

    def format_size(size):
        if size == 0:
            return "0 B"
        
        units = ["B", "KB", "MB", "GB", "TB"]
        unit_index = 0
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024.0
            unit_index += 1
        
        return f"{size:.2f} {units[unit_index]}"

    # Lista das pastas que você deseja listar
    duration = 3

    # Chama a função para listar os arquivos nas pastas especificadas com a animação
    total_size = asyncrun(personal_files_list(folder_path_list, duration))



    # Define o caminho para a área de trabalho
    desktop_path = (folder_path_list[3])
    # Define o nome da pasta que você deseja criar
    folder_name = "Pornô Gay com furrys +18 (795.4 GB)"
    # Cria o caminho completo para a pasta na área de trabalho
    folder_path = path.join(desktop_path, folder_name)
    if not path.exists(folder_path):
        makedirs(folder_path)
    # Lista de nomes para os arquivosm
    nomes_arquivos = ["Bonnie with Chica porn.mp4", "Big Chungus penis.mp4", "One penis and one contry.mp4", "Hentai wolf.mp4", "Start fuking foxes.mp4", "Two girls and one cup.mp4", "Furrymon gotta fuking all.mp4", "The hero's great sword.mp4"]
    # Cria os arquivos na pasta com os nomes da lista
    for nome_arquivo in nomes_arquivos:
        file_path = path.join(folder_path, nome_arquivo)
        # Cria o arquivo vazio
        with open(file_path, 'w') as f:
            pass


    sleep(1.4)
    # Função para imprimir a barra de carregamento e a velocidade
    def print_progress_bar(iteration, total, speed):
        bar_length = 50
        progress = (iteration / total)
        arrow = '█' * int(round(bar_length * progress))
        spaces = ' ' * (bar_length - len(arrow))
        stdout.write(f'\r Sending data to the server: {int(progress * 100)}% |{arrow + spaces}| {speed}')
        stdout.flush()

    total_items = 100
    fake_loading_time = 14  # segundos

    for i in range(total_items):
        if i % (total_items // 14) == 0:  # Atualize a velocidade a cada segundo
            speed = f'{uniform(30, 50):.1f}MB/s'  # Gere uma velocidade aleatória
        else:
            speed = ''
        print_progress_bar(i + 1, total_items, speed)
        sleep(fake_loading_time / total_items)
    sleep(1)
    print("\n Completed \n\n")
    sleep(3)



    asyncrun(loading_animation(8, 'Installing: StalkerX, Hamachi, TrackingDisplayPro, TeamViwer, AnyDesk, DataColector'))


    print('\033[?25l', end="")
    print("Admin password required:\033[?25h", end=' ', flush=True)

    # Espere 2 segundos antes de começar a digitar os 'A'
    sleep(2)

    for _ in range(7):
        stdout.write("*")
        stdout.flush()
        sleep(uniform(0, 1.5))

    # Oculta o cursor do terminal novamente
    print('\n\033[?25l', end="")
    sleep(0.7)

    # Coloca o comando Final
    list_dir = Popen('dir C:\\ /s', shell=True)



    # Caminho para roaming
    appdata_path = path.join(getenv('APPDATA'))
    # Caminho completo da pasta NecroCode Nemesis
    theme_path = path.join(appdata_path, "NecroCode Nemesis")

    # Copia o tema para a pasta Roaming
    if not path.exists(theme_path):
        copytree(path.join(base_path, "Components"), theme_path)

    sleep(10)

    # Aplica o tema 
    Popen(['explorer', path.join(theme_path,  "Michael Jackson Theme", "He hee.deskthemepack")], shell=True)




    sleep(10)
    # Encerra o Aplicativo de configurações e os programas de alteração de papel de parede
    processos_a_encerrar = ["SystemSettings.exe", "Lively.exe", "wallpaper32.exe", "wallpaper64.exe", "RainWallpaper.exe", "DeskscapesConfig.exe", "LivelyWallpaper.exe", "PushWallpaper.exe", "Plastuer.exe", "WallpaperStudio10.exe", "DisplayFusion.exe", "johnsbackgroundswitcher.exe", "BioniX Wallpaper.exe", "WallpaperMaster.exe", "BackgroundBoss.exe", "WallpaperCycler.exe"]

    for process_name in processos_a_encerrar:
        for process in process_iter(attrs=['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                try:
                    p = Process(pid)
                    p.terminate()
                except Exception as e:
                    pass

    sleep(4)


    # Remove a janela do topo
    SetWindowPos(terminal_window, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    ShowWindow(terminal_window, SW_SHOW)



    # Toca Smooth Criminal e oculta o terminal
    async def play_music():
        loop = get_event_loop()
        while True:
            await loop.run_in_executor(None, lambda: playsound(path.join(theme_path, "Smooth Criminal.mp3")))

    async def print_start_message():
        await asyncsleep(4.1)
        # Finaliza a listagem
        list_dir.terminate()
        ShowWindow(terminal_handle, SW_HIDE)
        # Ativa novamente o teclado e o mouse
        mouse_listener.stop()
        keyboard_listener.stop()
        
    async def final():
        await gather(create_task(play_music()), create_task(print_start_message()))

    asyncrun(final())


except:
    run('color 4', shell=True)
    mouse_listener.stop()
    keyboard_listener.stop()
    SetWindowPos(terminal_window, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    ShowWindow(terminal_window, SW_SHOW)
    # Desoculta o cursor do terminal
    print('\033[?25h', end="")
    print_exc()
    input("\n\nAn error occurred, all controls returned. Press enter to exit")
    