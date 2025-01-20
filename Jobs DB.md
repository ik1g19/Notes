---

database-plugin: basic

---

```yaml:dbfolder
name: new database
description: new description
columns:
  __file__:
    key: __file__
    id: __file__
    input: markdown
    label: File
    accessorKey: __file__
    isMetadata: true
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 1
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  recruiter:
    input: text
    accessorKey: recruiter
    key: recruiter
    id: recruiter
    label: recruiter
    position: 3
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 172
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  __outlinks__:
    key: __outlinks__
    id: __outlinks__
    input: outlinks
    label: Outlinks
    accessorKey: __outlinks__
    isMetadata: true
    isDragDisabled: false
    skipPersist: false
    csvCandidate: false
    position: 2
    isHidden: false
    sortIndex: 1
    width: 326
    isSorted: true
    isSortedDesc: true
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  employer:
    input: text
    accessorKey: employer
    key: employer
    id: employer
    label: employer
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 197
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  ongoing?:
    input: text
    accessorKey: ongoing?
    key: ongoing?
    id: ongoing?
    label: ongoing?
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 129
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  status:
    input: text
    accessorKey: status
    key: status
    id: status
    label: status
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 229
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
config:
  remove_field_when_delete_column: false
  cell_size: compact
  sticky_first_column: false
  group_folder_column: 
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: true
  show_metadata_tags: false
  source_data: tag
  source_form_result: "#job"
  source_destination_path: /
  row_templates_folder: /
  current_row_template: 
  pagination_size: 95
  font_size: 12
  enable_js_formulas: false
  formula_folder_path: /
  inline_default: false
  inline_new_position: last_field
  date_format: yyyy-MM-dd
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: false
  implementation: default
filters:
  enabled: false
  conditions:
```