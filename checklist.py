from datetime import datetime,date

destination_item={
    'beach': ['swimsuit','sunscreen','sunglasses','beach shoes','towel','sun hat'],
    'mountain': ['hiking shoes', 'windbreaker', 'trekking poles', 'insect repellent spray'],
    'city': ['comfortable shoes','portable charger','map or navigation app'],
    'cold': ['thick coat','thermal underwear','gloves','scarf']
}


basic_items=['ID/passport','toiletries','mobile phone and charger','common medicines','wallet']

def generate_clothing(days):
    return[f'clothing x{days}',f'underwear x{days}',f'socks x{days}']

def generate_checklist(destination_type,days):
    checklist={
        'basic':basic_items,
        'clothing':generate_clothing(days),
        'destination':destination_item.get(destination_type,[]),
        'custom':[],
        'packed':[]
    }
    return checklist

def show_checklist(checklist):
    print('\n📋 Current Packing List: ')
    for category,items in checklist.items():
        if category == 'packed':
            continue
        print(f'\n📦 {category}：')
        for item in items:
            packed_bag='✅'if item in checklist['packed'] else'❌'
            print(f'{packed_bag} {item}')

def mark_as_packed(checklist):
    while True:
        item=input('Please enter the item to mark as packed: ')
        if item.lower()=='break':
            break

        found=False
        for category in checklist:
            if category =='packed':
                continue
            if item in checklist[category]:
                found = True
                if item not in checklist['packed']:
                    checklist['packed'].append(item)
                    print(f'✅ Marked as packed: {item}')
                else:
                    print(f'⚠️ {item} already marked as packed')
                return
        if not found:
            print('⚠️ The item was not found. Please confirm that the input is correct.')

def add_custom_item(checklist):
    while True:
        item=input('Please enter the custom item you want to add: ')
        if item.lower() == 'break':
            break
        checklist['custom'].append(item)
        print(f'✅ Added:{item}')

def remove_item(checklist):
    while True:
        item=input('Please enter the item to remove: ')
        if item.lower()=='break':
            break

        found=False
        for category in ['custom','clothing','destination','basic']:
            if item in checklist[category]:
                checklist[category].remove(item)
                if item in checklist['packed']:
                    checklist['packed'].remove(item)
                print(f'🗑️ Deleted:{item}')
                return
        if not found:
            print('⚠️ The item was not found!')

def show_unpacked(checklist):
    print('\n📌 Unpacked: ')
    count=0
    for category in checklist:
        if category=='packed':
            continue
        for item in checklist[category]:
            if item not in checklist['packed']:
                print(f'❌ {item}')
                count += 1
    if count==0:
        print('✅ Everything is packed.')

def reset_packed_status(checklist):
    checklist['packed']=[]
    print('🔄 All packed markers cleared.')

def show_summary(checklist):
    total=0
    packed=len(checklist['packed'])
    for catagory in checklist:
        if catagory=='packed':
            continue
        total += len(checklist[catagory])
        remaining=total-packed
    print('\n📊 Summary: ')
    print(f'🎒 Total items: {total}')
    print(f'✅ Packed: {packed}')
    print(f'❌ Remaining: {remaining}')

def show_days_until_departure(departure_date):
    today=date.today()
    deldate=(departure_date-today).days
    format_date=departure_date.strftime('%d/%m/%Y')
    print(f'\n📅 Departure: {format_date}')
    if deldate>0:
        print(f'🕒 Days Until Departure: {deldate} days.')
    elif deldate==0:
        print('✈️ Today is the day! Have a nice trip!')
    else:
        print(f'🚀 It\'s been {abs(deldate)} days since I left')

def show_menu():
    print('\n========= Menu ========')
    print('1. View list')
    print('2. Mark as packed')
    print('3. Add custom item')
    print('4. Remove item')
    print('5. Show unpacked')
    print('6.Reset packed status')
    print('7.Show summary')
    print('8.View departure countdown')
    print('9.Exit')

def main():
    print('🌍 Welcome to the travel packing list!')

    valid_dest=['beach','mountain','city','cold']
    while True:
        destination_type=input('Please enter the destination type: ')
        if destination_type not in valid_dest:
            print('❌ Invalid destination type. Please try again.')
            continue
        else:
            break
    days=int(input('Please enter the number of days to check: '))


    departure_str=input('Please enter the departure date(DD/MM/YYYY): ')
    daparture_date=None
    formats=[
        "%Y-%m-%d", "%Y/%m/%d",
        "%d-%m-%Y", "%d/%m/%Y",
        "%Y.%m.%d", "%d.%m.%Y",
        "%Y %m %d", "%d %m %Y",
    ]
    for fmt in formats:
        try:
            departure_date=datetime.strptime(departure_str,fmt).date()
            break
        except ValueError:
            continue

    if departure_date is None:
        print('❌ Invalid departure date! Default is today.')
        departure_date=datetime.today().date()
    print(f'✔️ Departure date: {departure_date}')
    checklist=generate_checklist(destination_type,days)
    print('✅ This is your packing list!')
    show_menu()

    while True:
        choice = input('Please enter your choice: ')
        if choice=='menu'.lower():
            show_menu()
        elif choice=='1':
            show_checklist(checklist)
        elif choice=='2':
            mark_as_packed(checklist)
        elif choice=='3':
            add_custom_item(checklist)
        elif choice=='4':
            remove_item(checklist)
        elif choice=='5':
            show_unpacked(checklist)
        elif choice=='6':
            reset_packed_status(checklist)
        elif choice=='7':
            show_summary(checklist)
        elif choice=='8':
            show_days_until_departure(departure_date)
        elif choice=='9':
            print('👋 Have a nice trip!')
            break
        else:
            print('⚠ Please re-enter!')

if __name__ == "__main__":
    main()
