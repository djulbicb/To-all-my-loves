# Ionic without angular
**index.html**
```
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>

    <script type="module" src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.esm.js"></script>
    <script nomodule src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@ionic/core/css/ionic.bundle.css" />
</head>
<body>
    
    <ion-app>
        <ion-toolbar color="primary">
            <ion-title>Expense app</ion-title>
        </ion-toolbar>

        <ion-content>
            <ion-grid>
                <ion-row>
                    <ion-col size-md="6" offset-md="3">

                        <ion-card>
                            <ion-card-header>
                              <ion-card-title>Expense calculator</ion-card-title>
                            </ion-card-header>
                          
                            <ion-card-content>
                                <ion-item>
                                    <ion-label position="floating">Expense reason:</ion-label>
                                    <ion-input id="input-reason"></ion-input>
                                </ion-item>
                                <ion-item>
                                    <ion-label position="floating">Expense amount:</ion-label>
                                    <ion-input id="input-amount" type="number"></ion-input>
                                </ion-item>
                                <div class="ion-margin-vertical ion-text-right">
                                    <ion-button id="btn-clean" fill="outline" color="danger"><ion-icon name="trash-bin-outline"></ion-icon> Clear</ion-button>
                                    <ion-button id="btn-add" color="primary"><ion-icon name="add-circle-outline"></ion-icon> Add expense</ion-button>
                                </div>
                            </ion-card-content>
                          </ion-card>

                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size-md="6" offset-md="3">
                        <ion-list id="expenses-list"></ion-list>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size-md="6" offset-md="3">
                        <p>Total expense: <span id="expense-total">0</span>$</p>
                    </ion-col>
                </ion-row>
            </ion-grid>
        </ion-content>
    </ion-app>

    <script src="index.js"></script>
</body>
</html>           
```

**index.js**
```
console.log("Loaded");

const inpReason = document.querySelector("#input-reason");
const inpAmount = document.querySelector("#input-amount");
const btnClean = document.querySelector("#btn-clean");
const btnAdd = document.querySelector("#btn-add");

const expensesList = document.querySelector("ion-list");
const lblTotal = document.querySelector("#expense-total");

let total = 0;

function clear() {
    inpReason.value = "";
    inpAmount.value = 0;
}

btnClean.addEventListener("click", (event)=>{
    console.log(event);
    clear();
})


btnAdd.addEventListener("click", (ev)=> {
    const reason = inpReason.value;
    const amount = inpAmount.value;

    if (reason.trim().length === 0 || amount === 0) {
        myfunction("Invalid", "Check content. <3")
        return;
    }

    total = total + parseFloat(amount);

    const newItem = document.createElement('ion-item');
    newItem.textContent = reason + ': $' + amount;
    expensesList.appendChild(newItem);

    lblTotal.textContent = total;
    clear();
})

const myfunction = async function(header, content) {
    const alert = document.createElement('ion-alert');
    alert.cssClass = 'my-custom-class';
    alert.header = header;
    alert.subHeader = 'Subtitle';
    alert.message = content;
    alert.buttons = ['OK'];
  
    document.body.appendChild(alert);
    await alert.present();
  
    const { role } = await alert.onDidDismiss();
    console.log('onDidDismiss resolved with role', role);
  }
```