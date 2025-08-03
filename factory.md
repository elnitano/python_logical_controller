# Factory overview for this project
A short explanation of the factory.

More will come later.

## Overview
![Overview of the sorting plant.](/factory/overview.png)

Packages (Small, Medium, Large) will be placed at the green Emitter, run towards the scale.

The package will be weighted, and classified where it should be sorted, Thereafter run towards the sorting belt.

While package is on sorting belt, it should be tracked, to when the Sweeper arm for each respective package should go out.

First lane = Small Packages
Second lane = Medium Packages
Third lane = Large Packages

## Control Cabinet
![Control Cabinet to Start and Stop the Plant](/factory/control_cabinet.png)

Used to Start and Stop the Plant.

Start works as a Normally open switch (0 = False, 1 = True)
Stop works as a Normally closed switch (0 = True, 1 = False)

## Scale
![Scale of the sorting plant.](/factory/scale.png)

The scale is used to classify the product.

If package is below 4.5Kg its a Small Package

If package is between 4.5Kg and 6.5Kg its a Medium Package

If package is above 6.5Kg its a Large Package

## Sorting
![Sorting conveyors, with sweeper](/factory/sorting.png)

After the package has been classified into its category.

We need to sort this on the conveyor.

First attempt would be to utilize the Encoder bit.

We will create an empty list of first 1000 entries.

The sorted package will write to the first position in our list.

When Encoder bit is active, it should move the entire list 1 position forward.

Destinations:
 - First conveyor is for Small packages
 - Second conveyor is for Medium packages
 - Third conveyor is for Large packages