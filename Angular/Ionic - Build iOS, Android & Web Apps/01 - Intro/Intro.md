# Ionic
- Ionic crates crossplatform application based on same codebase.
- This is called Progressive Web Apps (PWAs).
- Ionic consists of Web Components. 
- Capacitor wraps webapp and creates native mobile apps
- Ionic has
    1. Platform-adaptive web components
    2. Tools to convert WebApp to NativeMobile App
- Ionic Framework were built with `stencil`. You can create your own components with stencil.js
- After that Capacitor or Cordova can be used to build cross-platform app
- Ionic works with vanillaJs, React, Vue...
- Ionic 4 uses browser functionality to create custom html elements. Ionic uses WebComponents

# Angular
- Client side (runs in browser) JS framework for building UI. 
- Angular uses TypeScript, which is JS superset
- Framework is set of tools, utility helpers that make process easier
- SPA (Single Page Applications)
- Download LTS version of NodeJS, currently NodeJS 17 doesnt work with Angular.

# Installation
- Install Ionic
```
npm install -g ionic
ionic start
# pick project name
# pick framework Angular
# when picking templates pick Blank, 
# when picking Appflow Sdk, no. Appflow is cloud service, its usable for free
cd project-name
ionic serve
```
- Install Visual studio code
```
code .

# Plugins
Angular Essentials
Material Icon Theme
```

When compiling you could compile JS to Java or ObjectC. Or wrap code into WebView Widget. Its a full screen browser.
Thats what is uses. Creates a web app shall that hosts ionic webapp.

## First app
**home.page.html**
```
<ion-header [translucent]="true">
  <ion-toolbar>
    <ion-title>
      Blank
    </ion-title>
  </ion-toolbar>
</ion-header>

<ion-content [fullscreen]="true">
  <div id="container">
    <p>{{ text }}</p>
    <ion-button color="primary" (click)="click()">Primary</ion-button>
  </div>
</ion-content>
```
**home.page.ts**
```
import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  text:string = "Hello";

  constructor() {}
  
  click() {
    this.text = "Hi hi :)";
    console.log("sss")
  }
}
```

# Angular CLI
- Install NodeJs you will get npm command
```
npm install -g @angular/cli
ng new my-dream-app
cd my-dreap-app
ng serve

# compile and bundle, creates dist folder
ng build
```
Main file is `main.ts`. Where its specified which module to bootstrap.
In import you dont have to specify .ts. Its automatically added.
**main.ts**
```
import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
```

Importing class is only available if class is exported. Angular works in module. Module is bundle of stuff.
Module will be compiled into constructor class. NgModule is a function, decorator which adds functionality.
NgModule adds metadata.
```
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent    # define all components we can use in module
  ],
  imports: [
    BrowserModule   # import other module in this module
  ],
  providers: [],
  bootstrap: [AppComponent] # Only used od bootstrap Modules. This is the component thats gonna be root component.
})
export class AppModule { }
```
**index.html**
Component is mounted on following html tag
```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>NgRefresher</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```
## Make a component
- Create subfolder `src/app/per sons`
- Define file `persons.component.ts`, `persons.component.html`
- Add component to AppModule. App module searches for it inside all of its module files

**persons.component.ts**
```
import { Component } from "@angular/core";

@Component({
    selector: 'persons',
    templateUrl: './persons.component.html',
})
export class PersonsComponent {
}
```
**persons.component.html**
```
<p>I &lt;3 you </p>
```
app.module.ts
```
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { PersonsComponent } from './persons/persons.component';

@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

## ngFor direktiva and properties
Directive ngFor is enabled by BrowserModule. Syntax `{{property}}` is called string interpolation
**persons.component.ts**
```
import { Component, Input } from "@angular/core";

@Component({
    selector: 'persons',
    templateUrl: './persons.component.html',
})
export class PersonsComponent {
    numbers: number[] = [1, 2, 3, 4]
    @Input() persons: string[] = [];
}
```
**persons.component.html**
```
<p>I &lt;3 you </p>
<ul>
    <li *ngFor="let p of persons">
        {{p}}
    </li>
</ul>
```
**app.component.html**
```
<persons [persons]="persons"></persons>
```
**app.component.ts**
```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  persons = ["Max", "John"]
  title = 'ng-refresher';
}
```

## Person input with names
**person-input.component.ts**
```
import { Component } from "@angular/core";
@Component({
    selector: "person-input",
    templateUrl: "./person-input.component.html",
    styleUrls: ["./person-input.component.css"]
})
export class PersonInputComponent {
    addPerson(personName:string) {
        console.log(personName)
    }
}
```
**person-input.component.html**
```
<label for="name">Person Name:</label>
<input id="name" type="text" #field>
<button (click)="addPerson(field.value)">Add person</button>
```
**app.module.ts**
```
import { PersonInputComponent } from './persons/person-input.component';

@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent,
    PersonInputComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
**app.component.html**
```
<person-input></person-input>
<persons [persons]="persons"></persons>
```

## Person input with property and emitter
**person-input.component.ts**
```
import { Component, EventEmitter, Output } from "@angular/core";

@Component({
    selector: "person-input",
    templateUrl: "./person-input.component.html",
    styleUrls: ["./person-input.component.css"]
})
export class PersonInputComponent {
    name:string = "";

    @Output() personCreated = new EventEmitter<string>();

    addPerson() {
        console.log(this.name);
        this.personCreated.emit(this.name);
    }
}
```
**person-input.component.html**
```
<label for="name">Person Name:</label>
<input id="name" type="text" [(ngModel)]="name">
<button (click)="addPerson()">Add person</button>
```
**app.component.html**
```
<person-input (personCreated)="onPersonCreate($event)"></person-input>
<persons [persons]="persons"></persons>
```
**app.component.ts**
```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  persons = ["Max", "John"]
  title = 'ng-refresher';

  onPersonCreate(name:string) {
    this.persons.push(name);
  }
}
```

## Binding with router and services
**app-routing.module.ts** - pored app.module.ts
```
import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { PersonInputComponent } from "./persons/person-input.component";
import { PersonsComponent } from "./persons/persons.component";

const routes: Routes = [
    { path: '', component: PersonsComponent},
    { path: 'input', component: PersonInputComponent}
]

@NgModule({
    imports: [ RouterModule.forRoot(routes)],
    exports: [ RouterModule ] // this is configured routerModuler from above
})
export class AppRoutingModule {

}
```

**app.module.ts**
```
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { PersonInputComponent } from './persons/person-input.component';
import { PersonsComponent } from './persons/persons.component';

@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent,
    PersonInputComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

**app.module.ts**

Add router module
```
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule
  ],
```

**app.component.html**
```
<router-outlet></router-outlet>
```

### Injectable Service
**persons.service.ts**
```
import { Injectable } from "@angular/core";

@Injectable({providedIn: 'root'})
export class PersonsService {
    persons: string[] = ['Max', 'Manuel', 'Anna'];

    addPerson(name:string) {
        this.persons.push(name);
    }
}
```
App needs to be aware of a service. There are two ways to do this
- Use `@Injectable({providedIn: 'root'})`
- Or in app.module.ts
```
  @NgModule({
  declarations: [
    AppComponent,
    PersonsComponent,
    PersonInputComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [PersonsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

**persons.component.ts**
```
import { Component, Input, OnInit } from "@angular/core";
import { PersonsService } from "./persons.service";

@Component({
    selector: 'persons',
    templateUrl: './persons.component.html',
})
export class PersonsComponent implements OnInit {
    
    persons: string[] = [];

    constructor( private personsService: PersonsService) {
        
    }

    ngOnInit(): void {
        this.persons = this.personsService.persons;
    }    
}
```
Its better to use ngOnInit than constructor cause of testing.

### Add a person to service
**person-input.component.ts**
```
import { Component, EventEmitter, Output } from "@angular/core";
import { PersonsService } from "./persons.service";

@Component({
    selector: "person-input",
    templateUrl: "./person-input.component.html",
    styleUrls: ["./person-input.component.css"]
})
export class PersonInputComponent {
    name:string = "";

    constructor(private personsService: PersonsService) {

    }

    addPerson() {
        console.log(this.name);
        this.personsService.addPerson(this.name);
        this.name = '';
    }
}
```

If you reload browser, app will refresh and loose all data stored in previous session (application state).
We have to use routes.

### Add Routing to conserve application state
**app.component.html**
```

<a [routerLink]="'/'">Person List</a>
<a routerLink="/">Person List</a>
<a routerLink="/input" href="/input">Input</a>
<hr>
<router-outlet></router-outlet>
```

## Remove person
**person.service.ts**
```
import { Injectable } from "@angular/core";
import { Subject } from "rxjs";

@Injectable({providedIn: 'root'})
export class PersonsService {
    // for emiting events
    personsChanged = new Subject<string[]>();
    persons: string[] = ['Max', 'Manuel', 'Anna'];

    addPerson(name:string) {
        this.persons.push(name);
        this.personsChanged.next(this.persons);
        console.log(this.persons);
    }

    removePerson(name: string) {
        this.persons = this.persons.filter(elem=> {
            return elem !== name
        })
        this.personsChanged.next(this.persons);
    }
}
```

**persons.component.ts**

Whenever you subsrive to custom Subject you have to unsubscribe
```
import { Component, Input, OnDestroy, OnInit } from "@angular/core";
import { Subscription } from "rxjs";
import { PersonsService } from "./persons.service";

@Component({
    selector: 'persons',
    templateUrl: './persons.component.html',
})
export class PersonsComponent implements OnInit, OnDestroy {
    
    persons: string[] = [];
    private personSubs: Subscription = new Subscription();

    constructor( private personsService: PersonsService) {
        
    }

    ngOnInit(): void {
        this.personsService.fetchPersons();
        this.personSubs = this.personsService.personsChanged.subscribe(newstuff => {
            this.persons = newstuff;
        })
    }    

    ngOnDestroy(): void {
        this.personSubs.unsubscribe();
    }

    onRemove (person: string) {
        this.personsService.removePerson(person);
    }
}
```

# Http requests
app.module.ts - `HttpClientModule`
```
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import {HttpClientModule} from '@angular/common/http';
import { AppComponent } from './app.component';
import { PersonInputComponent } from './persons/person-input.component';
import { PersonsComponent } from './persons/persons.component';

@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent,
    PersonInputComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
persons.component.html
```
<p>I &lt;3 you </p>
<p *ngIf="isLoading">Loading...</p>
<ul>
    <li *ngFor="let p of persons" (click)="onRemove(p)">
        {{p}}
    </li>
</ul>

```
persons.component.ts
```
import { Component, Input, OnDestroy, OnInit } from "@angular/core";
import { Subscription } from "rxjs";
import { PersonsService } from "./persons.service";

@Component({
    selector: 'persons',
    templateUrl: './persons.component.html',
})
export class PersonsComponent implements OnInit, OnDestroy {
    
    persons: string[] = [];
    isLoading: boolean = false;

    private personSubs: Subscription = new Subscription();

    constructor( private personsService: PersonsService) {
        
    }

    ngOnInit(): void {
        this.isLoading = true;
        this.personsService.fetchPersons();
        this.personSubs = this.personsService.personsChanged.subscribe(newstuff => {
            this.persons = newstuff;
            this.isLoading = false;
        })
    }    

    ngOnDestroy(): void {
        this.personSubs.unsubscribe();
    }

    onRemove (person: string) {
        this.personsService.removePerson(person);
    }
}
```

persons.service.ts
```
import { HttpClient } from "@angular/common/http";
import { Injectable, OnInit } from "@angular/core";
import { map, Subject } from "rxjs";

@Injectable({providedIn: 'root'})
export class PersonsService implements OnInit{
    // for emiting events
    personsChanged = new Subject<string[]>();

    constructor(private http: HttpClient) {
    }

    fetchPersons() {
        this.http.get<any>("https://swapi.dev/api/people")
        .pipe(map(resData => {
            return resData.results.map((c: { name: any; }) => c.name);
        }))
        .subscribe(transformedData => {
            this.personsChanged.next(transformedData);
        })
    }

    ngOnInit(): void {    
    }

    addPerson(name:string) {
        this.personsChanged.next(this.persons);
    }

    removePerson(name: string) {
        this.personsChanged.next(this.persons);
    }
}
```


