

# RESSOURCES : définir une ressource

# Ressource qui va être appelée avec le depends_on
resource "aws_iam_role" "exemple" {
  name = "toto"
}

# Dans l'exemple, "web" est le nom de notre service, on pourrait mettre n'importe quel autre nom à la place
resource "aws_instance" "web" {
  
  # for_each : permet de faire plusieurs instances différentes (avec des confs différentes)
  for_each = {
    a_group = "AMI-123"
    another_group = "AMI-DEBIAN"
  }
  # count : Va me faire 4 instances pareils
  count = 4
  ami = "AMI-123" # argument propre au provider

  instance_type = "t2.micro" 
  
  # Dépend de la fonction aws_iam_role, créer un lien entre différentes ressources
  depends_on = [
    aws_iam_role.exemple
  ]

  tags {
      toto = "valeur"
  }
}

resource "type" "name" {
  ami = var.image_id
}


# PROVIDERS : la liaison entre API service et ressource

provider "google" {
  project = "monProjet"
}


# VARIABLES : déclare une variable d'entrée

variable "image_id" {
  type = string
  default = "toto"
}
# String, number, bool
# list(string), set(Type), map(Type), object(key=valeur)
# tuple([... ])



#OUTPUT : valeur de sortie

output "instance_ip_privider" {
  value = "value"
}

# CLI //

# terraform [argument]

# init => initialise un répertoire de travail
# création nouvelle conf ou clonage => init

# plan => tester les modifs
# nécessaire pour atteindre l'état souhaité
# -> test notre conf -> ne persiste pas

# apply => appliquer les modifs
# nécessaire pour atteindre l'état souhaité
# -> applique notre conf -> persiste

# destroy => supprime notre infra -> persistant

# get => télécharge et met à jour des modules

# import => importe des ressources déjà existantes sur Terraform

# output => permet d'extraire la valeur d'une variable de sortie

# providers => donne des infos sur le fournisseur

# show => permet de fournir une sortie sous forme de fichier détat

# validate => permet de vérifier et valider la syntaxe d'un fichier .tf

