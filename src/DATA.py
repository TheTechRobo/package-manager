usage = ("Commands are:\n"
        "-h, --help: Display this help message.\n"
        "-v, --version: Display the version.\n"
        "install: Install a program.\n"
        "remove: Remove a program.\n"
        "list: Show information about a program.\n"
        "\n Commands like install, remove, and list, but NOT like -h, --version, etc MUST be the FIRST ARGUMENT. The program name MUST be the SECOND ARGUMENT. Example:\n"
        "    thetechrobo install palc, or\n"
        "    thetechrobo list mathmod\n"
        "\nThanks for using TheTechRobo's package manager!\n\n"
        "Error codes are: \n"
        "1 - General error; "
        "2 - Could not load API; "
        "3 - User does not want to initialise the package manager; "
        "4 - Could not find requested package; "
        "5 - User cancelled operation; "
        "0 - All operations successful."
)

vRaw = "v.0.0.1"
version = "This is TheTechRobo Package Manager (TTRPM) %s. Thanks for using!" % vRaw

unknown = "Could not understand what you mean. We'll show you the usage.\n%s" % usage
