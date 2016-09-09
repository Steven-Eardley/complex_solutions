#!/usr/bin/env bash

# Toggle between the A and B forked versions of submodules. It's probably best to rename 'A' and 'B' to
# the actual fork providers, e.g. different orgs on github.

# Function to return lower case text so we can be lazy with our inputs
function lc() {
    echo "$1" | tr '[:upper:]' '[:lower:]'
}

# Function to echo some useful submodule info
function sub_info() {
    # Show the URLs for the submodules
    cat .gitmodules
    # Print out the path and commit of submodules
    git submodule --quiet foreach 'echo $path `git rev-parse HEAD`'
}

# The github URL paths to our submodules
SUB1_A="url\/with\/escaped\/slashes"
SUB1_B="url2\/with\/escaped\/slashes"

# Check the args to determine which branch we are switching to
if [ $# -ne 1 ]; then
    echo "Wrong number of arguments supplied. Please specify the submodule provider: 'A' or 'B'."
    exit 1
fi

# the target submodule is $1 from the script arguments - check it's a valid value
SWITCHTO=$(lc $1)
if  [ $SWITCHTO != "a" -a $SWITCHTO != "b" ]; then
    echo "Please supply arguments 'A' or 'B'."
    exit 1
fi

# Print current state for info
echo -e 'Before:'
sub_info

# Rewrite the .gitmodules file using sed
echo -e "\nRewriting .gitmodules..."
if [ $SWITCHTO == "a" ]; then
    sed -i '' "s/$SUB1_B/$SUB1_A/" .gitmodules
elif [ $SWITCHTO == "b" ]; then
    sed -i '' "s/$SUB1_A/$SUB1_B/" .gitmodules
fi

# Sync the changes made to .gitmodules
git submodule sync --recursive

# Get any changes to the submodule
git submodule update --init --recursive

# Print the result
echo -e '\nAfter:'
sub_info

